# Assignment 4
# CS 1400
# Starter code by CS 1400 course staff
# Assignment completed by Jana Johnson


# This function rounds all of the numbers in a list.
# Note that Python rounding will round x.5 to the nearest even number for any x.
def round_list(number_list):
    for index in range(len(number_list)):
        number_list[index] = round(number_list[index])
    return number_list


# This function takes two integers and returns the larger of the two. If they are equal, neither is returned.
def choose_larger(num1, num2):
    if int(num1) > int(num2):
        return num1
    elif num1 < num2:
        return num2
    else:
        return None


# This function takes three sides of a triangle and classifies the triangle into three categories:
#   - Equilateral: all sides are equal
#   - Isosceles: two sides are equal
#   - Scalene: all sides are unequal
def triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles"
    else:
        return "Scalene"


# This function takes one string paramater and adds an "a" or "an" to the beginning of the string depending on whether the first letter is a vowel or not.
def add_a_or_an_to_word(word):
    if word[0] in "aeiou":
        return "an " + word
    else:
        return "a " + word


# This function behaves like the above function, with the exception: if the last letter of the parameter string is an 's', then add "any" to the beginning. Keep word combined into one string.
def add_a_or_an_or_any_to_word(word):
    if word[-1] == "s": # Any word ending in 's', add 'any'
        return "any " + word
    elif word[0] in "aeiou": # Any word starting with a vowel, add 'an'
        return "an " + word
    else: # Otherwise, add'a'.
        return "a " + word


# This Function takes three parameters:
#   1) [List] of numbers and strings
#   2) (int) or (str) that replaces itself with the value of the third parameter
#   3) (int) or (str)
# This function looks at each item using a loop. Each item in the list that is equal to the second parameter is replaced with the third parameter using the for loop pattern that works with an index
def replace_in_list(first_list, replaceable_list, last_list):
    for index in range(len(first_list)):
        if first_list[index] == replaceable_list:
            first_list[index] = last_list
    return first_list


# This function takes a sentence and replaces some of the words using their synonyms
def replace_word_with_synonym(word):
    synonyms = {
        "big": "vast",
        "important": "noteworthy",
        "quiet": "tranquil",
        "nice": "pleasant",
        "octagon": "octahedron",
        "quick": "prompt",
        "funny": "humorous",
        "kind": "benevolent",
        "fun": "exhilarating",
        "brave": "courageous",
        "exciting": "thrilling",
    }
    if word in synonyms:
        return synonyms[word]
    return word


# This function will take in a sentence and return a new sentence with some of the words replaced with their synonyms. Assumes the sentence is lowercase.
def thesaurus(sentence):
    sentence = sentence.split()
    for index in range(len(sentence)):
        sentence[index] = replace_word_with_synonym(sentence[index])
    return " ".join(sentence)


# ----------------------------------------------------------------------------------------------------------------------
# Main tests all the functions and reports on their results
# Report on what was tested and what the result was in the main function below.
def main():
    #print("Testing the round_list function")
    #print("Testing round_list([0, 0.1, 1.9]). Expecting a result of [0, 0, 2] and computed a result of", str(round_list([0, 0.1, 1.9])) + ".")
    #print("Testing round_list([0.5, 1.5, 2.5]). Expecting a result of [0, 2, 2] and computed a result of", str(round_list([0.5, 1.5, 2.5])) + ".")

    # Test chose_larger function
    print(' ---------------------------------------------------------------------------------------')
    print(' Testing the choose_larger function:')
    print(' ---------------------------------------------------------------------------------------')
    print("    | (num1 > num2 = num1)         |  Expecting: 10           |  Result: ", str(choose_larger(5, 10)) + "           |")
    print("    | (num1 < num2 = num2)         |  Expecting: 10           |  Result: ", str(choose_larger(10, 5)) + "           |")
    print("    | (num1 == num2 = None)        |  Expecting: None         |  Result: ", str(choose_larger(10, 10)) + "         |")
    print("    | (whole #  vs  decimal #)     |  Expecting: 2.3          |  Result: ", str(choose_larger(2.3, 1.0)) + "          |")

    # Test triangle_type function
    print(' ---------------------------------------------------------------------------------------')
    print(' Testing the triangle_type function:')
    print(' ---------------------------------------------------------------------------------------')
    print("    | (side1 == side2 == side3)    |  Expecting: Equilateral  |  Result: ", str(triangle_type(10, 10, 10)) + "  |")
    print("    | (side1 == side2)             |  Expecting: Isosceles    |  Result: ", str(triangle_type(10, 10, 5)) + "    |")
    print("    | (side1 == side3)             |  Expecting: Isosceles    |  Result: ", str(triangle_type(10, 5, 10)) + "    |")
    print("    | (side2 == side3)             |  Expecting: Isosceles    |  Result: ", str(triangle_type(5, 10, 10)) + "    |")
    print("    | (side1 != side2 != side3)    |  Expecting: Scalene      |  Result: ", str(triangle_type(10, 5, 2)) + "      |")

    # Test add_a_or_an_to_word function
    print(' ---------------------------------------------------------------------------------------')
    print(' Testing the add_a_or_an_to_word function:')
    print(' ---------------------------------------------------------------------------------------')
    print("    | (word: vowel a)              |  Expecting: an apple     |  Result: ", str(add_a_or_an_to_word("apple")) + "     |")
    print("    | (word: no =n-vowel)          |  Expecting: a chair      |  Result: ", str(add_a_or_an_to_word("chair")) + "      |")
    print("    | (word: vowel e)              |  Expecting: an elf       |  Result: ", str(add_a_or_an_to_word("elf")) + "       |")
    print("    | (word: other non-vowel)      |  Expecting: a purse      |  Result: ", str(add_a_or_an_to_word("purse")) + "      |")
    print("    | (word: vowel 0)              |  Expecting: an octagon   |  Result: ", str(add_a_or_an_to_word("octagon")) + "   |")

    # Test add_a_or_an_or_any_to_word function
    print(' ---------------------------------------------------------------------------------------')
    print(' Testing the add_a_or_an_or_any_to_word function:')
    print(' ---------------------------------------------------------------------------------------')
    print("    | (word: with s)               |  Expecting: any waves    |  Result: ", str(add_a_or_an_or_any_to_word("waves")) + "    |")
    print("    | (word: with vowel and s)     |  Expecting: any utahns   |  Result: ", str(add_a_or_an_or_any_to_word("utahns")) + "   |")
    print("    | (word: only vowel)           |  Expecting: an earring   |  Result: ", str(add_a_or_an_or_any_to_word("earring")) + "   |")
    print("    | (word: no vowel)             |  Expecting: a bicycle    |  Result: ", str(add_a_or_an_or_any_to_word("bicycle")) + "    |")

    # Test replace_in_list function
    print(' ---------------------------------------------------------------------------------------')
    print(' Testing the replace_in_list function:')
    print(' -------------------------------------------------------------------------------------------------------------------------')
    print("    | (Replace '4' with '2')       |  Expecting: [0, 1, 'two', 3, 2, 5]      |  Result:", str(replace_in_list([0,1, 'two', 3, 'four', 5], 2, 'four')) + "      |")
    print("    | (Replace '1' with 'eight')   |  Expecting: [0, 'eight', 2, 3, 2, 5]    |  Result:", str(replace_in_list([0,1,2, 3,4, 5], 1, 'eight')) + "         |")
    print("    | (Replace 'four' with '5')    |  Expecting: [0, 1, 2, 3, 5, 5]          |  Result:", str(replace_in_list([0,1,2, 3,'four', 5], 'four', 5 )) + "               |")


    # Test thesaurus function
    print(' -------------------------------------------------------------------------------------------------------------------------')
    print(' Testing the thesaurus function:')
    print(' -------------------------------------------------------------------------------------------------------------------------')
    print("    | Test Sentence 1: My dad has a big important meeting     |  Result: ", str(thesaurus("My dad has a big important meeting")) + "           |")
    print("    | Test Sentence 2: exciting times are upon us             |  Result: ", str(thesaurus("exciting times are upon us")) + "                    |")
    print("    | Test Sentence 3: That octagon is nice and quiet         |  Result: ", str(thesaurus("That octagon is nice and quiet")) + "       |")
    print("    | Test Sentence 4: the quick brave fox is funny           |  Result: ", str(thesaurus("The quick brave fox is funny")) + "          |")



if __name__=="__main__":
    main()
