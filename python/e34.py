import datetime
import math

FACTORIAL_DICT = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}


def digit_fact_sum(input_number):
    global FACTORIAL_DICT
    sum = 0
    for i in digits(input_number):
        sum += FACTORIAL_DICT[i]
    return sum


def digits(input_number):
    digits_list = list()
    total_digits = math.ceil(math.log10(input_number))
    for i in range(1, total_digits + 1):
        modded_input = input_number % pow(10, 1 + total_digits - i)
        this_digit = math.floor(modded_input / (pow(10, total_digits - i)))
        digits_list.append(this_digit)
    return digits_list


def main():
    sum = 0
    range_limit = 6 * math.factorial(9)
    for i in range(3, range_limit):
        dfs = digit_fact_sum(i)
        if i == dfs:
            sum += i
    print(sum)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
