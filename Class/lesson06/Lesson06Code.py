
def price_admission(age):
    if age < 5:
        return "Free"
    elif age <= 17:
        return "$5"
    else:
        return "$10"


def num_check(number):
    if number > 0:
        return "Positive Number"
    if number == 0:
        return "Zero"
    else:
        return "Negative Number"


def weather_check(sky):
    if sky == "sunny":
        return "It's a sunny day!"
    elif sky == "cloudy":
        return "It's a cloudy day!"
    else:
        return "It's a rainy day!"


def main():
    print(price_admission(9))

# Dunder methods are double underscores.
# So, when this fle is run, it saves the variable name as __name__
# and checks to see if it is __main__. If so, it runs the main function.
# https://docs.python.org/3/reference/datamodel.html#special-method-names
if __name__ == "__main__":
    main()

