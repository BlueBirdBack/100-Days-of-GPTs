class ArtistMindscape(Scene):
    def __init__(self):
        super().__init__("ArtistMindscape", "You enter the mindscape of a painter struggling with creative block and depression. The once vibrant world of the artist's imagination has been reduced to a bleak, monochromatic wasteland.")
        self.memories_discovered = 0
        self.critic_defeated = False
        self.core_memory_found = False

    def enter(self, game):
        # Display the patient's background
        # Describe the color-drained and surreal landscape filled with unfinished and abandoned art pieces
        # Prompt the player to explore and find the fragmented memories

    def handle_input(self, game, user_input):
        if user_input.lower() in ["examine", "look"]:
            # Describe the unfinished art pieces and the bleak atmosphere
            # Hint at the location of the fragmented memories
        elif user_input.lower() in ["explore", "search"]:
            # Randomly discover a fragmented memory
            self.discover_memory(game)
        elif user_input.lower() in ["confront", "challenge"]:
            # Initiate the confrontation with the critic creature
            self.confront_critic(game)
        elif user_input.lower() in ["find", "locate"]:
            # Attempt to find the repressed core memory
            self.find_core_memory(game)
        elif user_input.lower() in ["exit", "leave"]:
            if self.core_memory_found:
                # Return to the office
                game.transition_to_scene("Office")
                # Update the artist's mental state and display Watson's glitch
            else:
                # Prompt the player to continue exploring and resolve the artist's block
        else:
            # Display default response for unrecognized input
        return True

    def discover_memory(self, game):
        # Randomly select a fragmented memory from a predefined list
        # Display the memory as a brief, vivid flashback related to the failed art exhibition and harsh critique
        # Increment the memories_discovered counter
        # If all memories are discovered, piece together the story of the artist's shattered confidence
        # Hint at the location of the repressed core memory

    def confront_critic(self, game):
        if not self.critic_defeated:
            # Display the description of the critic creature and its harsh taunts
            # Engage in a dialogue or challenge that represents the artist's inner self-doubt and fear of failure
            # Provide choices for the player to counter the critic's words with positive affirmations
            # Update the game state to mark the critic as defeated
            self.critic_defeated = True
        else:
            # Display a message indicating that the critic has already been confronted

    def find_core_memory(self, game):
        if self.critic_defeated and self.memories_discovered >= 3:
            # Display the repressed core memory of the childhood trauma related to the artist's passion
            # Prompt the player to make a choice that reframes the experience positively
            # Update the game state to mark the core memory as found
            self.core_memory_found = True
        else:
            # Display a message indicating that more memories need to be discovered or the critic needs to be confronted
