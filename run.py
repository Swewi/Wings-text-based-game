import sys
import time
from story import wings_text


class Wings:
    """
    Wings class for a text-based adventure game.
    """

    def __init__(self):
        """
        Initialise the Wings game by creating an instance of the Wings class,
        using the 'wings_text' dictionary to define the
        game's storyline and choices.
        """
        self.story_description = wings_text

    def type_text(self, text, delay=0.02):
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
        print("""
                                   ____,
                                  /  / ]
                                 /  /  ]
    |      ,======--_________,. '  /___]   __        ___
    |_____/____|___)                 _,.>  \ \      / (_)_ __   __ _ ___
   <|          |        G-Wings ,. '`       \ \ /\ / /| | '_ \ / _` / __|
    |\         |          ,. '`              \ V  V / | | | | | (_| \__ \'
    | `,_______|____,. '`                     \_/\_/  |_|_| |_|\__, |___/
        ^          \                                           |___/
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
                    raise ValueError("Cannot be empty or only spaces.")

                # Checks if the username contains special characters
                if not username.isalnum():
                    raise ValueError("Should contain only letters and nums.")

                # Checks if the username is too short or too long
                if len(username) < 3 or len(username) > 20:
                    raise ValueError("Length should be between 3 and 20 chars.")

                return username

            except ValueError as e:
                print("Please try again.\n")

    def restart_game(self):
        """
        Function to restart the game, regardless of outcome.
        """
        while True:
            restart_choice = input("\nSo, did you enjoy yourself? Do you want to play again?(yes/no): ").strip().lower()
            if restart_choice.startswith('y'):
                self.start_game()
                break
            elif restart_choice.startswith('n'):
                self.type_text("""
    **------------------------------------------------------------**
                       Thanks for playing!
    **------------------------------------------------------------**
                   """)
                break
            else:
                print("\nUmm what?!?! I need a 'yes' or 'no'.")

    def play_game(self, current_step="start"):
        """
        Main function to play game text.
        """
        while current_step:
            step = self.story_description[current_step]
            step_text = step["step_text"]
            options = step["options"]
            outcome = step.get("outcome")

            # Display the current step's text
            print(step_text)

            # Display the options
            if outcome == "success":
                self.type_text("""
**----------------------------------------------------------------------------**
        ╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬
        ║  │ │││││ ┬├┬┘├─┤ │ └─┐│
        ╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘o

        You landed safely and survived your first major incident.
        On your way home you stop at the local fish and chips shop
        for a fish supper!

        After the days adventure you spend the weekend relaxing and
        recovering so you can be ready for your final assesment,
        surely that will be easy after this...
**----------------------------------------------------------------------------**
                    \n""")
                self.restart_game()
                break
            elif outcome == "failure":
                self.type_text("""
**----------------------------------------------------------------------------**
        Did you survive?  Did you disapear like Amelia Earhart?
        What happened to you and your plane?
        These are questions that people ask for years, long after
        the inquest has concluded...
**----------------------------------------------------------------------------**
                    \n""")
                self.restart_game()
                break
            if options:
                choice = input("Enter your choice (either 1 or 2): "
                               ).strip().lower()
                while choice not in ["1", "2"]:
                    print("\nInvalid choice. Please enter 1 or 2.")
                    choice = input("\nEnter your choice (either 1 or 2): ").strip().lower()

                current_step = options[f"option_{choice}"]
            else:
                current_step = None

    def start_game(self):
        """
        Intro, rules, are you ready querry.  Validity of entered data.
        """
        self.display_intro()
        while True:
            play_choice = input("\nAre you ready to play? (yes/no): "
                                ).strip().lower()

            if play_choice.startswith('y'):
                user_name = self.get_username()
                self.type_text(f"""
                       Welcome {user_name.capitalize()}!""")
                print("""
         Taking off early in the morning, you have a fairly simple
         'out and return' flight planned.  This will be your last flight
         before the final assesement.  You are so close to your commercial
         pilots licence, you can almost taste it.  Landing safely at the end
         of your 'out' section of the flight, you park and go find some lunch,
         and maybe, more importantly, a bathroom!

         After a sandwich and a cup of tea, you get ready to take off on your
         way home.  This should be a nice, smooth flight home.
                      """)
                self.type_text(f"""
         The Air Traffic Controller is a friend of yours, their parting
         comment 'See you next weekend {user_name.capitalize()}, I'm looking forward to
         celebrating with you.  Good luck mate!'.
                """)
                self.play_game()
                break
            elif play_choice.startswith('n'):
                print("\nWell this is awkward, don't you want to get home?")
                print("Are you sure you don't want to play? Type 'yes' then hit enter to play\n")
            else:
                print("Invalid choice. Enter 'yes' or 'no'")


if __name__ == "__main__":
    """
    Creates an instance of the Wings class, initiates the game.
    """
    game = Wings()

    game.start_game()