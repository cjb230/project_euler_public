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
    global PRIMES_DICT
    prime_index = 4
    next_prime = generate_prime(prime_index)
    while next_prime < 1001:
        prime_index += 1
        next_prime = generate_prime(prime_index)
    possible_b = {v for v in PRIMES_DICT.values() if v < 1000}
    longest_run_length = 0
    longest_run_a = -1000
    longest_run_b = -1
    for this_b in possible_b:
        for a in range(-1000, 1000):
            n = 0
            while True:
                x = (n * (n + a)) + this_b
                if not(is_prime(x)):
                    break
                else:
                    if n > longest_run_length:
                        longest_run_length = n
                        longest_run_a = a
                        longest_run_b = this_b
                    n += 1

    print(longest_run_a * longest_run_b)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
