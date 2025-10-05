# Guessing Game
# Code/debugging activity adapted from Bob McNabb
import random

def guessing_game():
    # pick a random number for the user to guess
    rand = random.randint(1, 100)

    guess = input("Guess a number between 1 and 20: ")
    guess = int(guess) # number needs to be an integer

    while guess != rand: # if the guess is not equal to the random number, you have to guess again
        # flipped > opperand to <
        if int(guess) < int(rand): # if the guess is too high, tell the user
            print("Too low. Guess again.")
        # Added else if statement to allow for correct guess beneath in the else section.
        elif int(guess) > int(rand): # if the guess is too low, tell the user
            print("Too high. Guess again.")
        # added the final "you guessed it"
        else:
            print("You guessed it!")

        guess = input("Enter a new guess: ")

    return "You got it! The number was: " + str(rand)


def main():
    guessing_game()


if __name__ == "__main__":
    main()