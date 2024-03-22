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
                  You will be challenged at every step.
                          So choose wisely

                            Good luck!!
            """)

    