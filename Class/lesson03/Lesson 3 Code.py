# take in a number and return that number mult. by 2
def double(number):
    return number * 2

# doubled_num = double(100)
# print("100 doubled is:", doubled_num)
# print(double(10947382))

# takes in two numbers and returns the sum
def add(num1, num2):
    result = num1 + num2
    return result

# print(add(2, 9))
# print(add(-1, 5))
# print(add(21813094, 9145824085))

# calculate the amount of paint needed
def paint_needed(wall_area):
    return wall_area / 400

def rect_area(length, width):
    return length * width

area = rect_area(20, 30)
gallons_needed = paint_needed(area)
print(gallons_needed)