import datetime

PRIMES_FOUND = {2}
ERATOSTHENES_CHECKED = 2


def eratosthenes_next():
    global PRIMES_FOUND
    global ERATOSTHENES_CHECKED
    next_check = ERATOSTHENES_CHECKED
    next_prime_found = False

    while next_prime_found is False:
        next_check = next_check + 1
        check_sqrt = next_check ** 0.5
        next_may_be_prime = True
        for this_prime in PRIMES_FOUND:
            if this_prime <= check_sqrt:
                if next_check % this_prime == 0:
                    next_may_be_prime = False
                    break
        if next_may_be_prime is True:
            PRIMES_FOUND.add(next_check)
            break

    ERATOSTHENES_CHECKED = next_check
    return next_check


def main():
    sum_so_far = 2
    next_prime_found = eratosthenes_next()

    print("Started first method: " + str(datetime.datetime.now()))
    while next_prime_found < 2000000:
        sum_so_far += next_prime_found
        next_prime_found = eratosthenes_next()
    print(sum_so_far)
    print("Finished first method: " + str(datetime.datetime.now()))


if __name__ == "__main__":
    main()
