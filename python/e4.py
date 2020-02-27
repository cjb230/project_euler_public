import math

UPPER_SEARCH_LIMIT = 999 ** 2
LOWER_SEARCH_LIMIT = 100 ** 2


def is_three_digit_product(test_number):
    # a nicer way to do this would be to find the prime factors of the test number, and see if they can be assembled
    # into two three-digit numbers
    for i in range(100, 1000):
        if test_number % i == 0:
            x = test_number / i
            if 99 < x < 1000:
                print(str(test_number) + " = " + str(i) + " * " + str(x))
                return True
    return False


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


def main():
    for i in range(UPPER_SEARCH_LIMIT, LOWER_SEARCH_LIMIT - 1, -1):
        if is_palindrome(i):
            if is_three_digit_product(i):
                break


if __name__ == "__main__":
    main()
