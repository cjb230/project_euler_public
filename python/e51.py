import datetime
import math

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


def in_primes_dict(check_value):
    global PRIMES_DICT
    if check_value < 2:
        return False
    if check_value > PRIMES_DICT[len(PRIMES_DICT)]:
        return False
    result = False
    min_key = 1
    max_key = len(PRIMES_DICT)
    while True:
        if min_key + 1 == max_key:
            if check_value > PRIMES_DICT[min_key]:
                if check_value < PRIMES_DICT[max_key]:
                    break
            elif check_value == PRIMES_DICT[min_key]:
                result = True
                break
        else:
            mid_key = int(math.floor(min_key + ((max_key - min_key) / 2)))
        this_test_value = PRIMES_DICT[mid_key]
        if this_test_value > check_value:
            max_key = mid_key
        elif this_test_value < check_value:
            min_key = mid_key
        elif this_test_value == check_value:
            result = True
            break
    return result


def is_prime(check_value):
    global PRIMES_DICT
    result = False
    dict_max = PRIMES_DICT[len(PRIMES_DICT)]
    if check_value > dict_max:
        while True:
            next_prime_index = len(PRIMES_DICT) + 1
            next_prime = generate_prime(next_prime_index)
            if next_prime == check_value:
                result = True
                break
            elif next_prime > check_value:
                break
    elif check_value < dict_max:
        result = in_primes_dict(check_value)
    elif check_value == dict_max:
        result = True
    return result


def main():
    i = 0
    for seq_num, seq_prime in PRIMES_DICT.items():
        if seq_prime > 56004:
            seq_prime_string = str(seq_prime)

            if seq_prime_string.count('0') > 1 or seq_prime_string.count('1') > 1 or seq_prime_string.count('2') > 1:
                print(seq_prime)
                i += 1
    print(i)


if __name__ == "__main__":
    start = datetime.datetime.now()
    print(prime_by_number(78499))
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
