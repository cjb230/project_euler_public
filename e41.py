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
    prime_factors = dict()
    residual = factorisation_requested
    next_prime_check_index = 1
    while residual > 1:
        this_prime_power = 0
        while residual % PRIMES_DICT[next_prime_check_index] == 0:
            this_prime_power += 1
            residual = int(residual / PRIMES_DICT[next_prime_check_index])
        if this_prime_power > 0:
            prime_factors[PRIMES_DICT[next_prime_check_index]] = this_prime_power
        next_prime_check_index += 1
    return prime_factors

def is_pandigital(test_number):
    return_value = True
    test_string = str(test_number)
    digits = len(test_string)

    for i in range(1,  digits + 1):
        if str(i) not in test_string:
            return_value = False
            break

    return return_value


def main():
    max_pp = 0
    i = 1

    # a number with the digits 1-9 is divisible by 9, so cannot be prime.
    # same with a number with the digits 1-8 (digit sums = 45 and 36 respectively)
    max_pandigital = 7654321

    this_prime = prime_by_number(i)

    while this_prime < max_pandigital:
        if is_pandigital(this_prime):
            max_pp = this_prime
            print(max_pp)
        i += 1
        this_prime = prime_by_number(i)
    print(max_pp)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
