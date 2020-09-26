""" Strangely, using @lru_cache memoization on the is_left_truncatabale() and is_right_truncatable() functions seems to
slow things down, not speed them up.

Having looked at a couple of other solutions on the thread, fastest thing is probably to build up numbers that are left-
truncatable, and separately build up numbers that are right-truncatable, then look for numbers that occur in both. This
could be done by generating n+1 digit candidates from n-digit truncatable numbers, trimming out the non-truncatable
numbers generated, then looking for numbers that occur in the left- and right-truncatable lists.
"""
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


def is_truncatable(candidate):
    if candidate < 11:
        return False
    else:
        return is_left_truncatable(candidate) and is_right_truncatable(candidate)


def is_left_truncatable(candidate):
    if is_prime(candidate):
        if candidate >= 10:
            return is_left_truncatable(int(math.floor(candidate / 10)))
        else:
            return True
    else:
        return False


def is_right_truncatable(candidate):
    if is_prime(candidate):
        if candidate >= 10:
            return is_right_truncatable(int(str(candidate)[1:]))
        else:
            return True
    else:
        return False


def main():
    prime_index = 1
    truncatables_found = 0
    truncatables_sum = 0
    while truncatables_found < 11:
        next_prime = prime_by_number(prime_index)
        if is_truncatable(next_prime):
            truncatables_found += 1
            truncatables_sum += next_prime
            print(str(truncatables_found) + ': ' + str(next_prime))
        prime_index += 1
    print('Sum = ' + str(truncatables_sum))


if __name__ == "__main__":
    main()
