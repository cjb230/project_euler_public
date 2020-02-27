import math
import datetime

PRIMES_DICT = {1: 2, 2: 3, 3: 5}


def generate_prime(prime_index_requested):
    global PRIMES_DICT
    next_prime_index = len(PRIMES_DICT) + 1
    next_prime_candidate = PRIMES_DICT[len(PRIMES_DICT)] + 2
    while next_prime_index <= prime_index_requested:
        check_limit = math.ceil(next_prime_candidate ** 0.5)
        next_factor_index = 2
        valid_candidate = True
        while PRIMES_DICT[next_factor_index] <= check_limit:
            if next_prime_candidate % PRIMES_DICT[next_factor_index] == 0:
                valid_candidate = False
                break
            next_factor_index += 1
        if valid_candidate is True:
            PRIMES_DICT[next_prime_index] = next_prime_candidate
            next_prime_index += 1
        next_prime_candidate = next_prime_candidate + 2
    return PRIMES_DICT[prime_index_requested]


def prime_by_number(prime_requested):
    global PRIMES_DICT
    if prime_requested > len(PRIMES_DICT):
        return generate_prime(prime_requested)
    else:
        return PRIMES_DICT[prime_requested]


def prime_factors(factorisation_requested):
    global PRIMES_DICT
    prime_factors_found = dict()
    residual = factorisation_requested
    next_prime_check_index = 1
    while residual > 1:
        this_prime_power = 0
        while residual % prime_by_number(next_prime_check_index) == 0:
            this_prime_power += 1
            residual = int(residual / prime_by_number(next_prime_check_index))
        if this_prime_power > 0:
            prime_factors_found[PRIMES_DICT[next_prime_check_index]] = this_prime_power
        next_prime_check_index += 1
    return prime_factors_found


def count_factors(test_number):
    inputs_prime_factors = prime_factors(test_number)
    total_factors = 1
    for key, value in inputs_prime_factors.items():
        total_factors = total_factors * (value + 1)
    return total_factors


def main():
    triangle_iter = 0
    triangle_number = 0
    while True:
        triangle_iter += 1
        triangle_number += triangle_iter
        triangle_number_total_factors = count_factors(triangle_number)
        if triangle_number_total_factors > 500:
            print(triangle_iter, ": ", triangle_number)
            break


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(duration.total_seconds())
