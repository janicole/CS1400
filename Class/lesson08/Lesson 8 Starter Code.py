# Here is some starter code to use for Lesson 8
import random


def main():
    # guessing game from lab 2
    print("Welcome to the psychic guessing game!")

    for count in range(10):
        player_guess = int(input('What is your guess (from 1 to 10)? '))
        computer_die_roll = random.randint(1, 10)
        print("You guessed", player_guess, "and the roll was", computer_die_roll)


if __name__ == "__main__":
    main()