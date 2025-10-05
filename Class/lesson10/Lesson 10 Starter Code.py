# Warm up
def bigger_than_ten(number):
    pass # Replace this line with your code


# Debugging example code
def odd(number):
    return number % 2 == 1


def delete_odd_numbers_from_list(number_list):
    for index in range(len(number_list)):
        if odd(number_list[index]):
            del number_list[index]
    return number_list


def replace_one_with_number(number_list, new_number):
    for i in range(len(number_list)):
        number = number_list[i]
        if number == 1:
            number_list[number] = new_number
    return number_list


def main():
    numbers = list(range(10))
    # even_numbers = delete_odd_numbers_from_list(numbers)
    # print("Testing delete_odd_numbers_from_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]). Expecting [0, 2, 4, 6, 8], got:", even_numbers)
    # ones_replaced = replace_one_with_number(numbers, -5)
    # print("Testing replace_one_with_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], -5). Expecting [0, -5, 2, 3, 4, 5, 6, 7, 8, 9]. Got:", ones_replaced)

    numbers2 = [1, 2, 1, 3, -4, 1]
    ones_replaced = replace_one_with_number(numbers2, -5)
    print("Testing replace_one_with_number([1, 2, 1, 3, -4, 1], -5). Expecting [-5, 2, -5, 3, -4, -5]. Got:", ones_replaced)


if __name__ == "__main__":
    main()