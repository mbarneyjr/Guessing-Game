from __future__ import print_function
import random
import time
import termcolor

BLACK = "black"
WHITE = "white"
BLUE = "blue"
PURPLE = "purple"
RED = "red"
YELLOW = "yellow"
GREEN = "green"

COLORS = [BLACK, WHITE, BLUE, PURPLE, RED, YELLOW, GREEN]

def randomize_answer():
    to_guess = [None] * 5
    for i in range(0,5):
        to_guess[i] = COLORS[random.randrange(0,7)]
    return to_guess

def check_guess(guess, to_guess):
    if guess == to_guess:
        return (5, 0)
    right_color = 0
    right_spot = 0
    for i in range(0,5):
        if to_guess[i] in guess:
            if guess[i] == to_guess[i]:
                right_spot += 1
            else:
                right_color += 1
    return (right_spot, right_color)

def make_guess(guess, to_guess):
    if len(guess) < 5:
        print("Invalid Guess")
        return False, False
    result = check_guess(guess, to_guess)
    return result

def print_colors(colors):
    for color in colors:
        highlight = color
        text_color = 'grey'
        if color == 'purple': highlight = 'magenta'
        if color == 'black': highlight = 'grey'; text_color = 'white'
        print(termcolor.colored(color.ljust(7), text_color, 'on_' + highlight), end=' ')

def get_guess():
    guess = []
    print("Your options are: ", end='')
    print_colors(COLORS)
    print('')
    while len(guess) < 5:
        input = ''
        while len(guess) < 5:
            input = raw_input("What would you like to guess: ")
            guesses = input.split(' ')
            if len(guess) + len(guesses) > 5:
                print("You can't guess more than 5 times.")
            else:
                for g in guesses:
                    if g in COLORS:
                        guess.append(g)
                    elif g == 'quit':
                        return 'quit'
                    else:
                        print(g + " is not valid, it will not be included")
    return guess

def display_history(history):
    print("HISTORY".center(62, "="))
    print("GUESS".center(35), end='')
    print("RIGHT COLOR   RIGHT SPOT")
    for i in range(len(history['guess'])):
        print_colors(history['guess'][i])
        print(str(history['right_color'][i]).ljust(14), end='')
        print(str(history['right_spot'][i]).ljust(12), end='')
        print("")
    print("".center(62, "="))


def play(answer):
    history = dict()
    history['guess'] = []
    history['right_color'] = []
    history['right_spot'] = []

    done = False
    guess_number = 0
    while not done and guess_number < 10:
        print("Guess number " + str(guess_number+1))

        if len(history['guess']):
            display_history(history)

        user_guess = get_guess()
        if user_guess == 'quit':
            break
        right_spot, right_color = make_guess(user_guess, answer)

        history['guess'].append(user_guess)
        history['right_color'].append(right_color)
        history['right_spot'].append(right_spot)

        if right_spot == 5:
            print("YOU WIN!")
            done = True
        else:
            guess_number += 1
        print("\n\n\n")

    if guess_number >= 10 or done != True:
        print("You lose")
        print("The answer was: ", end='')
        print_colors(answer)
        print('')

def main():
    answer = randomize_answer()
    play(answer)

if __name__ == "__main__":
    main()


