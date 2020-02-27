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
        while residual % prime_by_number(next_prime_check_index) == 0:
            this_prime_power += 1
            residual = int(residual / prime_by_number(next_prime_check_index))
        if this_prime_power > 0:
            prime_factors[prime_by_number(next_prime_check_index)] = this_prime_power
        next_prime_check_index += 1
        if prime_by_number(next_prime_check_index) > pow(residual, 0.5):
            prime_factors[residual] = 1
            break
    return prime_factors


def sum_set(input_set):
    sum = 0
    for this_num in input_set:
        sum += this_num
    return sum


def proper_divisors(input_number):
    my_prime_factors = prime_factors(input_number)
    previous_divisor_set = {1}
    next_divisor_set = set()
    for this_prime in my_prime_factors:
        for previous_divisor in previous_divisor_set:
            for i in range(0, my_prime_factors[this_prime] + 1):
                next_divisor_set.add(previous_divisor * pow(this_prime, i))
        previous_divisor_set = next_divisor_set.copy()
        next_divisor_set = set()
    if input_number > 1:
        previous_divisor_set.remove(input_number)
    return previous_divisor_set


def main():
    sum = 0
    for i in range(1, 10001):
        divisor_sum = sum_set(proper_divisors(i))
        if divisor_sum != i:
            if sum_set(proper_divisors(divisor_sum)) == i:
                print(str(i) + " : " + str(divisor_sum))
                sum += i
    print(sum)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
