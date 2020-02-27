TARGET = 600851475143
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
    global PRIMES_FOUND
    global TARGET
    target_remaining = TARGET
    iter_limit = TARGET ** 0.5
    targets_factors = set()
    next_prime = eratosthenes_next()

    while target_remaining > 1 and next_prime < iter_limit:
        if target_remaining % next_prime == 0:
            print("Factor: " + str(next_prime))
            target_remaining = target_remaining / next_prime
            targets_factors.add(next_prime)
        else:
            next_prime = eratosthenes_next()


if __name__ == "__main__":
    main()
