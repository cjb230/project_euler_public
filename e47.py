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
    prime_factors = set()
    residual = factorisation_requested
    next_prime_check_index = 1
    while residual > 1:
        this_prime_power = 0
        while residual % prime_by_number(next_prime_check_index) == 0:
            this_prime_power += 1
            residual = int(residual / prime_by_number(next_prime_check_index))
        if this_prime_power > 0:
            prime_factors.add(prime_by_number(next_prime_check_index))
        next_prime_check_index += 1
    return prime_factors


def main():
    found = False
    i = 210
    fourth_last = 0
    third_last = 0
    second_last = 0
    last = 0

    while not found:
        i += 1
        if i % 20000 == 0:
            print("====" + str(i) + "====")
        if len(prime_factors(i)) == 4:
            fourth_last = third_last
            third_last = second_last
            second_last = last
            last = i
            if i - fourth_last == 3:
                found = True

    print(str(fourth_last) + " : " + str(prime_factors(fourth_last)))
    print(str(third_last) + " : " + str(prime_factors(third_last)))
    print(str(second_last) + " : " + str(prime_factors(second_last)))
    print(str(last) + " : " + str(prime_factors(last)))
    print(fourth_last)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
