import datetime
import math


def mod_pow(input_number, n_digits):
    result = 1
    modulo_at = pow(10, n_digits)
    for i in range(1, input_number + 1):
        result = (result * input_number) % modulo_at
    return result


def main():
    mod_sum = 0
    n_digits = 10
    modulo_at = pow(10, n_digits)
    for i in range(1, 1001):
        mod_sum = (mod_sum + mod_pow(i, n_digits)) % modulo_at
    print(mod_sum)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
