
# Write a function that takes in a parameter that is a
# list of strings. The function should print all of the
# strings that start with the letter 'a'.
# Also, the function should return True if something was
# printed or False if nothing was printed (i.e., if there
# are no strings in the list that start with 'a').


def print_a_strings(words):
    something_printed = False
    for word in words:
        if word[0] == 'a':
            print(word)
            something_printed = True
    return "Something Printed: " + str(something_printed)

def main():
    words = ['hello', 'world', 'goodbye', 'apple', 'banana', 'ape']
    print(print_a_strings(words))


if __name__ == '__main__':
    main()