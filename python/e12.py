import math
import datetime


def factors(test_number):
    factor_set = {1, test_number}
    test_limit = math.ceil(test_number ** 0.5) + 1
    for x in range(1, test_limit):
        if test_number % x == 0:
            factor_set.add(x)
            factor_set.add(int(test_number / x))
    return factor_set


def main():
    triangle_iter = 0
    triangle_number = 0
    while True:
        triangle_iter += 1
        triangle_number += triangle_iter
        triangle_number_factors = factors(triangle_number)
        if len(triangle_number_factors) > 500:
            print(triangle_iter, ": ", triangle_number, ": ", str(sorted(triangle_number_factors)))
            break


if __name__ == "__main__":
    print(datetime.datetime.now())
    main()
    print(datetime.datetime.now())
