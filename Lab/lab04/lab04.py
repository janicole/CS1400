import random
#
# correct_guess = 0
#
# print("Welcome to the psychic guessing game!")
# for count in range(10):
#     player_guess = int(input('What is your guess (from 1 to 10)? '))
#     computer_die_roll = random.randint(1,10)
#     print("You guessed", player_guess, "but the roll was", computer_die_roll)
#
#     if player_guess == computer_die_roll:
#         correct_guess += 1
#         print("You Got it!")
#
#     print ("You guessed", str(correct_guess), "correctly")


def is_big_number(number):
    if number > 10000:
        return "big"
    elif number <= 0:
        return int(number) * -1
    else:
        return "small"

print(is_big_number(-50))
