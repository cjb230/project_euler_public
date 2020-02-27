import datetime
import math

POWER_DICT = {0: 0, 1: 1, 2: 32, 3: 243, 4: 1024, 5: 3125, 6: 7776, 7: 16807, 8: 32768, 9: 59049}


def digit_list(input_number):
    digits_list = list()
    total_digits = math.ceil(math.log10(input_number))
    for i in range(1, total_digits + 1):
        modded_input = input_number % pow(10, 1 + total_digits - i)
        this_digit = math.floor(modded_input / (pow(10, total_digits - i)))
        digits_list.append(this_digit)
    return digits_list


def digit_power_sum(input_number):
    global POWER_DICT
    sum = 0
    digits = digit_list(input_number)
    for digit in digits:
        sum += POWER_DICT[digit]
    return sum


def main():
    sum = 0
    upper_limit = 1 + (6 * 59049)
    for i in range(1, upper_limit):
        if i == digit_power_sum(i):
            sum += i
            print("Found: " + str(i))
    print("Sum = " + str(sum))


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
