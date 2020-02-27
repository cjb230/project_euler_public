import math
import datetime


def is_palindrome(test_number):
    number_is_palindrome = True
    digits = math.ceil(math.log10(test_number))
    checks_to_perform = math.floor(digits / 2)
    test_string = str(test_number)
    for i in range(1, checks_to_perform + 1):
        if test_string[i-1] != test_string[-i]:
            number_is_palindrome = False
            break
    return number_is_palindrome


def str_rev(input_string):
    return input_string[::-1]


def main():
    result = 0
    for i in range(1, 1000001):
        if is_palindrome(i):
            bin_str = str(bin(i)[2::])
            if bin_str == str_rev(bin_str):
                result += i
    print(result)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
