# Guessing Game

This is a simple guessing game where you have to guess the pattern of 5 colors.

I made this modelled after a physical board game; I want to develop an agent to play this game optimally.

## Dependencies

Currently this project only depends on the python package `termcolor`, used for coloring the display.

## How To Play

A pattern of 5 colors is randomly generated, and you have 10 chances to guess the correct pattern. There are seven possible colors, and the pattern may have repeating colors.

When you run the `guess.py` script, you will be presented with something like this:

```
Guess number 1
Your options are: ['black', 'white', 'blue', 'purple', 'red', 'yellow', 'green']
What would you like to guess:
```

You may type the entire pattern in one line:

```
blue blue blue blue blue
```

 or you may enter each color in one at a time.

```
What would you like to guess: blue
What would you like to guess: blue
What would you like to guess: blue
What would you like to guess: blue
What would you like to guess: blue
```

The order you enter the colors in matters, since you must match the pattern.

Once you give your first guess, you will be presented with a history of your guesses. Along with each guess, you will see some feedback on how well you guessed:

```
Guess number 5
===========================HISTORY============================
               GUESS               RIGHT COLOR   RIGHT SPOT
black  white  blue   purple red    4             0
blue   black  purple white  red    2             2
blue   black  white  red    purple 0             4
blue   black  white  red    yellow 0             4
==============================================================
Your options are: ['black', 'white', 'blue', 'purple', 'red', 'yellow', 'green']
What would you like to guess:
```

- The `GUESS` column will list the pattern you guessed, in order.
- The `RIGHT COLOR` column will tell you how many colors you got right, but aren't in the right spot.
- The `RIGHT SPOT` column will tell you how many colors you got right, and in the right spot.

If you type "quit" as an answer, you will leave the game.