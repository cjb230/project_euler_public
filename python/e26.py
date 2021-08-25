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
    all_prime_factors = dict()
    residual = factorisation_requested
    next_prime_check_index = 1
    while residual > 1:
        this_prime_power = 0
        while residual % PRIMES_DICT[next_prime_check_index] == 0:
            this_prime_power += 1
            residual = int(residual / PRIMES_DICT[next_prime_check_index])
        if this_prime_power > 0:
            all_prime_factors[PRIMES_DICT[next_prime_check_index]] = this_prime_power
        next_prime_check_index += 1
    return all_prime_factors


def reciprocal_pattern(div):
    dividend = 1
    divisor = div
    iterations = 0
    step_results = dict()
    while dividend < divisor:
        dividend *= 10
    while True:
        if dividend < divisor:
            dividend *= 10
        quotient = dividend // divisor
        remainder = dividend % divisor
        dividend = remainder
        iterations += 1
        this_result = (quotient, remainder)
        if iterations > 1 and this_result in step_results.values():
            break
        else:
            step_results[iterations] = this_result
    reciprocal_pattern = ''
    for this_key, this_value in step_results.items():
        reciprocal_pattern += str(this_value[0])
    return reciprocal_pattern, len(step_results)


def main():
    x = prime_by_number(169)
    longest_repeat_length = 0
    for i in range(7, 1001):
        pf = prime_factors(i)

        # ignore numbers that will generate terminating decimals
        if (len(pf) == 2 and 2 in pf and 5 in pf) or (len(pf) == 1 and (2 in pf or 5 in pf)):
            continue
        repeating_pattern, step_result = reciprocal_pattern(i)
        if len(repeating_pattern) > longest_repeat_length:
            longest_repeat_length = len(repeating_pattern)
            i_for_longest_pattern = i
    print(i_for_longest_pattern)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
