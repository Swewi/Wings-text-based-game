# Wings
## Can you survive?

[Link to live Website](https://wings-text-based-game-866d46ea2c76.herokuapp.com/)
---

![Screenshoot of image generated in amiresponsive.](assets/images/readme/responsive.png)

## Purpose

"Wings" is a text-based adventure, with retro vibes, written and executed using Python and run within Code 
Institutes mock terminal using the Heroku platform.

It is an interactive game, that the user interacts with by selecting from two options, each option has a consequence
of some sort, some are 'win' outcomes, some result in 'loose' outcomes, and some keep the adventure going.  It is,
in essence, a 'choose your own' adventure.

## How to play

The game is based on "Choose your own adventure" books from the 80's and 90's, you can read more about
the books here: [Wikipedia](https://en.wikipedia.org/wiki/Choose_Your_Own_Adventure)

#### Steps for playing:
* Upon entering the game space you are asked if you want to proceed.
* Promted to enter your name, there are several validation stages to ensure a valid name entry, each will repromt if error triggered.
* Enter the game space.
* Promted to start making your choices.
* The last step repeats until you end the adventure through either success or failure.
* A different conclussion shows depending on success or failure.
* You are promted to choocse between restart or stop.
* If you restarted the game loops back to the beginning.

## Features

### Exhisting Features

#### Welcome Screen

* You are greeted with an ascii-art image, and a 'typewriter' style printed message welcoming you and inviting you to play the game.
* A goal statement is also printed.

![Screenshot of the Welcome screen](assets/images/readme/start-screen.png)
<br>

#### Start Game

* After selecting 'yes' the game begins.
* You are promted with a username entry, here there are multiple validation steps to ensure valid entry.
* If you selected 'no' there is a querry if this was accurate.

![Screenshoot of the Start game screen](assets/images/readme/welcome-screen.png)
<br>

#### Story

* After a valid name entry you are greeted and introduced to the outline of the game.
* There is a little background text here explaining where you are.
* Then you find yourself making the decisions, the input required is based on binary, option 1 or 2, your choice will 
lead on to success or failure.

![Screenshot of option selection](assets/images/readme/options-menu.png)
<br>

#### Conclusion

* As you progress through the story you will reach 'end points', some of these are win conditions, some are loose conditions.
* Both have unique statements on completion.
* After you have seen a completion screen you are presented with an option to play again, or quit.

![Screenshot of win condition](assets/images/readme/success.png)
<br>

![Screenshot of loose condition](assets/images/readme/failure.png)
<br>

![Screenshot of play again option](assets/images/readme/conclusion.png)
<br>
