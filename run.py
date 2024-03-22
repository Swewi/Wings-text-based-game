import sys
import time

from story import wings_text

class Wings:
    """
    Wings class for a text-based adventure game.
    """
def __init__(self):
        """
        Initialize the Wings game.
        It creates an instance of the Wings game, using the
        'wings_text' dictionary to define the game's storyline and
        choices.
        """
        self.story_description = story_description

def type_text(self, text, delay=0.03):
        """
        Print text with a typing effect.
        """
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def display_intro(self):
        """
        Display the game's introduction.
        """
        # Credit for ASCII art: https://asciiart.website/index.php?art=transportation/airplanes adapted by me

    print("""
                                   ____,
                                  /  / ]
                                 /  /  ]
    |      ,======--_________,. '  /___]     __    __ _                 
    |_____/____|___)                 _,.>   / / /\ \ (_)_ __   __ _ ___ 
   <|          |        G-Wings ,. '`       \ \/  \/ / | '_ \ / _` / __|
    |\         |          ,. '`              \  /\  /| | | | | (_| \__ \
    | `,_______|____,. '`                     \/  \/ |_|_| |_|\__, |___/
      ^          \                                               |___/  
     (_)        (_)
    """)
    self.type_text("""
**----------------------------------------------------------------------------**
                G'day and welcome to "Wings" - an adventure
           that will challenge your sanity and flying expertise.
**----------------------------------------------------------------------------**
        """)
        print("""
         The goal of the game is to succesfully land your aircraft!
                    Will you accept the challenge?
            """)

    def get_username(self):
        """
        Prompt and validate user entered name.
        """
        while True:
            try:
                username = input("\nEnter your name: ").strip().lower()

                # Checks if the username is empty or contains only spaces
                if not username.strip():
                    raise ValueError("Username cannot be empty or contain only spaces.")

                # Checks if the username contains special characters
                if not username.isalnum():
                    raise ValueError("Username should contain only letters and numbers.")

                # Checks if the username is too short or too long
                if len(username) < 3 or len(username) > 20:
                    raise ValueError("Username length should be between 3 and 20 characters.")  

                return username

            except ValueError as e:
                print("Please try again.\n")

    def restart_game(self):
        """
        Function to restart the game, regardless of outcome.
        """
        while True:
            restart_choice = input("\nSo did you enjoy yourself? Do you want to play again?(yes/no): ").strip().lower()
            if restart_choice.startswith('y'):
                self.start_game()
                break
            elif restart_choice.startswith('n'):
                self.type_text("""
    **------------------------------------------------------------**
                       Thanks for playing!!
    **------------------------------------------------------------**
                   """)
                break
            else:
                print("\nUmm what?!?! I need a 'yes' or 'no'.")

    