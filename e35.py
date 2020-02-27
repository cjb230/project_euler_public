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


def rotate_num(orig_num):
    if orig_num > 9:
        tens_power = pow(10, math.floor(math.log10(orig_num)))
        remainder = orig_num % tens_power
        first_digit = int((orig_num - remainder) / tens_power)
        return (10 * remainder) + first_digit
    else:
        return orig_num


def main():
    generate_prime(78498)  # primes to one million
    potential_circular_primes = dict()
    potential_circular_primes[1] = set()
    potential_circular_primes[2] = dict()
    potential_circular_primes[3] = dict()
    potential_circular_primes[4] = dict()
    potential_circular_primes[5] = dict()
    potential_circular_primes[6] = dict()

    for this_prime in PRIMES_DICT.values():
        if this_prime > 9:  # anything with an even number or a five has a non-prime rotation
            has_forbidden_digit = False
            digit_sum = 0
            this_prime_string = str(this_prime)
            for this_digit in this_prime_string:
                if this_digit in ('2', '4', '5', '6', '8', '0'):
                    has_forbidden_digit = True
                    break
                digit_sum += int(this_digit)
            if not has_forbidden_digit:
                if digit_sum in potential_circular_primes[len(this_prime_string)]:
                    potential_circular_primes[len(this_prime_string)][digit_sum].append(this_prime)
                else:
                    potential_circular_primes[len(this_prime_string)][digit_sum] = [this_prime]

        else:
            potential_circular_primes[1].add(this_prime)

    circular_prime_count = 4  # the single-digit numbers
    for digit_length in range(2, 7):
        for this_sum, this_prime_list in potential_circular_primes[digit_length].items():
            for this_prime in this_prime_list:
                all_rotations_present = True
                next_rotation = rotate_num(this_prime)
                while next_rotation != this_prime:
                    if next_rotation not in this_prime_list:
                        all_rotations_present = False
                    next_rotation = rotate_num(next_rotation)
                if all_rotations_present:
                    circular_prime_count += 1
    print(circular_prime_count)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
