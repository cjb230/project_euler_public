import datetime
import math
import itertools

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


def main():
    four_digit_primes = list(prime_by_number(x) for x in range(169, 1230))
    permutations = dict()
    for this_prime in four_digit_primes:
        this_perm = "".join(sorted(str(this_prime)))
        if this_perm in permutations:
            permutations[this_perm].append(this_prime)
        else:
            permutations[this_perm] = [this_prime]

    short_permutations = list()
    for key, value in permutations.items():
        if len(value) < 3:
            short_permutations.append(key)
    for this_perm in short_permutations:
        del permutations[this_perm]

    for these_perms in permutations.values():
        for this_combination in itertools.combinations(these_perms, 3):
            if this_combination[2] - this_combination[1] == this_combination[1] - this_combination[0]:
                print(this_combination)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
