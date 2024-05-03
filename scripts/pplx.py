"""
This script lets you run a range of GPTs from the "100 Days of GPTs" project using Perplexity AI's API, no ChatGPT needed.
"""

import os
import sys
import time
import re
import concurrent.futures
from typing import Dict, List, Optional
from dotenv import load_dotenv
from openai import OpenAI


# Constants for model names, https://docs.perplexity.ai/docs/model-cards
MODELS = [
    "llama-3-sonar-small-32k-chat",
    "llama-3-sonar-large-32k-chat",
    "llama-3-8b-instruct",
    "llama-3-70b-instruct",
    "mixtral-8x7b-instruct",
]

# This variable is used to store the conversation history between the user and the AI model.
conversation_history = {}


class GroqScript:
    """Interact with the Groq API."""

    def __init__(self):
        load_dotenv()
        self.pplx_api_key = os.getenv("PPLX_API_KEY")
        if not self.pplx_api_key:
            raise ValueError("The PPLX_API_KEY environment variable is not set.")
        self.client = OpenAI(
            api_key=self.pplx_api_key, base_url="https://api.perplexity.ai"
        )

    def get_completion(
        self, prompt: str, model: str, system_prompt: str = None
    ) -> Optional[str]:
        """Get a completion from the Groq API."""
        start_time = time.time()
        try:
            # Create a separate conversation history for each model
            if model not in conversation_history:
                conversation_history[model] = []

            messages = conversation_history[model] + [
                {"role": "user", "content": prompt}
            ]
            if system_prompt:
                messages.insert(0, {"role": "system", "content": system_prompt})
            response = self.client.chat.completions.create(
                messages=messages,
                model=model,
            )

            end_time = time.time()
            print(f"{model}: {end_time - start_time:.2f} seconds")

            response_content = response.choices[0].message.content
            conversation_history[model].append({"role": "user", "content": prompt})
            conversation_history[model].append(
                {"role": "assistant", "content": response_content}
            )

            return response_content
        except Exception as e:  # pylint: disable=broad-except
            # Consider using logging.error here
            print(f"Error fetching completion for model {model}: {e}")
            return None

    def get_completions(
        self, prompt: str, models: List[str], system_prompt: str = None
    ) -> Dict[str, str]:
        """Get completions from the Groq API for multiple models."""
        # start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            futures = {
                executor.submit(
                    self.get_completion, prompt, model, system_prompt
                ): model
                for model in models
            }
            results = {
                futures[future]: future.result()
                for future in concurrent.futures.as_completed(futures)
            }
        # end_time = time.time()
        # print(f"Time taken to fetch completions: {end_time - start_time:.2f} seconds")
        return results

    def construct_system_prompt(self, day_param: int) -> str:
        """
        Construct the system prompt for the given day.

        This method reads the instructions from the markdown file for the given day and returns the trimmed instructions.
        """
        try:
            parent_dir = os.path.dirname(os.path.dirname(__file__))
            file_name = None

            for file in os.listdir(parent_dir):
                if os.path.isfile(os.path.join(parent_dir, file)):
                    if re.match(rf"Day-{day_param}-.*.md", file):
                        file_name = os.path.join(parent_dir, file)
                        break
            print(file_name)

            if file_name:
                with open(file_name, "r", encoding="utf-8") as f:
                    file_content = f.read()
                start = file_content.find("### Instructions") + len("### Instructions")
                end = file_content.find("### Conversation starters")
                instructions = file_content[start:end].strip()

                first_line_end = instructions.find("\n")
                last_line_start = instructions.rfind("\n")

                if first_line_end != -1 and last_line_start != -1:
                    trimmed_instructions = instructions[
                        first_line_end + 1 : last_line_start  # noqa: E203
                    ]
                else:
                    trimmed_instructions = ""  # or instructions

                return trimmed_instructions.strip()
            else:
                return ""
        except FileNotFoundError:
            print(f"Error: No instructions found for day {day_param}.")
            return None

    def gather_input(self) -> str:
        """
        Gather user input for the prompt.

        This method reads lines of input from the user until they type 'Q' to finish.
        """
        print("Enter your prompt (type 'Q' to finish):")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "Q":
                break
            lines.append(line)
        return "\n".join(lines)

    def main(self, day_param: int):
        """Run the main functionality of the script."""
        global conversation_history
        while True:
            prompt = self.gather_input()
            start_time = time.time()
            if len(prompt.strip()) == 0:
                conversation_history = {}
                break
            system_prompt = self.construct_system_prompt(day_param)
            if system_prompt is None:
                print(f"Error: No system prompt found for day {day_param}.")
                return
            results = self.get_completions(prompt, MODELS, system_prompt)

            for model, result in results.items():
                print("-" * 60)
                print(f"Turn: {len(conversation_history[model]) // 2}")
                print(f"Model: {model}\n\n{result}\n")

            end_time = time.time()
            print(f"Total time taken: {end_time - start_time:.2f} seconds")

    @staticmethod
    def validate_arguments():
        """Validate the command line arguments."""
        if len(sys.argv) < 2:
            print("Usage: python run_script.py <day>")
            sys.exit(1)
        try:
            return int(sys.argv[1])
        except ValueError:
            print("Error: Day must be a number.")
            sys.exit(1)


if __name__ == "__main__":
    day = GroqScript.validate_arguments()
    base_script = GroqScript()
    base_script.main(day)
