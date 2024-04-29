import os
import re


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set the path to the README.md file in the parent directory
readme_path = os.path.join(os.path.abspath(os.path.join(script_dir, "..")), "README.md")

# Read the current contents of the README.md file
with open(readme_path, "r", encoding="utf-8") as file:
    readme_content = file.read()

# Find the start of the GPT table
table_line = "| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |"
start_index = readme_content.find(table_line) + len(table_line)

# Get the list of GPT directories starting from Day 77
gpt_dirs = [
    d for d in os.listdir("./") if d.startswith("Day-") and int(d.split("-")[1]) >= 97
]
# gpt_dirs = sorted(gpt_dirs, reverse=True)
gpt_dirs = sorted(gpt_dirs, key=lambda x: int(x.split("-")[1]), reverse=True)
# e.g. ['Day-87-StockNet.md', 'Day-86-Imager.md', 'Day-85-PicDescribe.md', 'Day-84-FalloutLeaks.md', 'Day-83-MNISTro.md', 'Day-82-Promptopia.md', 'Day-81-Gemini-Pro.md', 'Day-80-NewsHub.md', 'Day-79-Claire.md', 'Day-78-ABChallenger.md', 'Day-77-Mindaze.md']
print(gpt_dirs)
# Generate the new GPT table data
table_data = []
for gpt_dir in gpt_dirs:
    day = int(gpt_dir.split("-")[1])  # e.g. 77

    gpt_file_path = os.path.join(
        os.path.abspath(os.path.join(script_dir, "..")), gpt_dir
    )
    with open(gpt_file_path, "r", encoding="utf-8") as file:
        gpt_content = file.read()

    profile_pic_match = re.search(r"!\[Profile Picture\]\((.*?)\)", gpt_content)
    profile_pic = profile_pic_match.group(1).strip() if profile_pic_match else ""

    name_match = re.search(r"### Name\n\n(.*)", gpt_content)
    name = name_match.group(1).strip() if name_match else ""

    link_match = re.search(r"\*\*GPT Link:\*\* (.*)", gpt_content)
    link = link_match.group(1).strip() if link_match else ""

    description_match = re.search(r"### Description\n\n(.*)", gpt_content)
    description = description_match.group(1).strip() if description_match else ""

    row = {
        "Day": day,
        "Profile⠀Picture": f'<img src="{profile_pic}" width="96" height="96" style="border-radius:50%">',
        "Name": f"[{name}]({link})",
        "Description": f"[{description}](./{gpt_dir})",
    }
    line = f"| {row['Day']} | {row['Profile⠀Picture']} | {row['Name']} | {row['Description']} |"

    table_data.append(line)

new_table = "\n".join(table_data)
print(new_table)

# Replace the existing GPT table with the new one
updated_readme = (
    readme_content[:start_index]
    + "\n"
    + new_table
    + "\n"
    + readme_content[start_index + 1 :]
)

# Write the updated README.md file
with open(readme_path, "w", encoding="utf-8") as file:
    file.write(updated_readme)
