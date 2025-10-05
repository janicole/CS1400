# Here is some starter code to use for Lesson 8
import random

# add up all the numbers from 1 to the specified number
def add_numbers(number):
    # step 1: initialize an "empty" accumulator variable
    running_sum = 0
    # step 2: loop over elements and update accumulator variable
    for value in range(number + 1):
        running_sum += value # same thing as: running_sum = running_sum + value
    # step 3: return the accumulator variable - BE CAREFUL OF INDENTATION
    return running_sum

def count_a(text):
    # step 1: initialize an "empty" accumulator variable
    number_of_a = 0
    # step 2: loop over elements and update accumulator variable
    for character in text:
        if character == 'a':
            number_of_a += 1
    # step 3: return accumulator variable
    return number_of_a

# return all of the occurrences of the letter 'a' as a new string
# option 1
def build_a(text):
    only_a = "" # step 1
    for character in text:
        if character == "a":
            only_a += character # step 2
    return only_a # step 3

# option 2
def build_a(text):
    only_a = "" # step 1
    for index in range(len(text)):
        if text[index] == "a":
            only_a += "a" # step 2
    return only_a # step 3



# **********  LISTS  ****************  LISTS  ****************  LISTS  *************
# write a function that returns a list with only positive numbers
# given a list of numbers
# option 1: loop over elements of list directly
def only_positives(numbers):
    positive_numbers = [] # step 1
    for number in numbers:
        if number > 0:
            positive_numbers.append(number) # step 2
    return positive_numbers # step 3

# option 2: loop over index
def only_positives(numbers):
    positive_numbers = [] # step 1
    for index in range(len(numbers)):
        if numbers[index] > 0:
            positive_numbers.append(numbers[index]) # step 2
    return positive_numbers # step 3



# **********  LISTS  ****************  LISTS  ****************  LISTS  *************
# return a list of only names longer than 5 letters given a list of names
def find_long_names(names):
    long_names = [] # step 1
    for name in names:
        if len(name) > 5:
            long_names.append(name) # step 2
    return long_names # step 3



def main():
    print("testing only_positives")
    print("with [-1, 2, -3, 4]. expecting: [2, 4]. got:", only_positives([-1, 2, -3, 4]))
    print("with [-1, -3]. expecting: []. got:", only_positives([-1, -3]))
    # print("testing build_a")
    # print("with 'i am a cat'. expecting 'aaa'. got:", build_a('i am a cat'))
    # print("testing add_numbers")
    # print("with 5. Expecting 15. Got:", add_numbers(5))
    # print("with 3. Expecting 6. Got:", add_numbers(3))
    # guessing game from lab 2
    #print("Welcome to the psychic guessing game!")

    # option 1: let the user keep guessing until they win
    # player_guess = int(input('What is your guess (from 1 to 10)? '))
    # computer_die_roll = random.randint(1, 10)
    #
    # while player_guess != computer_die_roll:
    #     player_guess = int(input("incorrect. Guess again: "))
    #
    # print("you win!")

    # option 2: play a new game until user wins
    # keep_playing = True
    #
    # while keep_playing:
    #     player_guess = int(input('What is your guess (from 1 to 10)? '))
    #     computer_die_roll = random.randint(1, 10)
    #     if player_guess == computer_die_roll:
    #         print("you win!")
    #         keep_playing = False




if __name__ == "__main__":
    main()