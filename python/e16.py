import datetime
import math


def digit_sum(input_number):
    # not keen on using a string method here, so we're staying with routines from math.
    result = 0
    digits = math.ceil(math.log10(input_number))
    for i in range(1, digits + 1):
        this_digit = int(((input_number % pow(10, i)) - (input_number % pow(10, i - 1))) / pow(10, i - 1))
        result += this_digit
    return result


if __name__ == "__main__":
    start = datetime.datetime.now()
    print(digit_sum(pow(2, 1000)))
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")