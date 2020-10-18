"""
This runs fine, and in about 0.4s, but it's surprising that putting the test for divisibility by 17 as the first test
makes it slower, not faster.
A depth-first search, starting from the least significant digits, seems like it would be faster.
"""
import datetime
import itertools


def main():
    digits = list(range(0, 10))
    pandigital_totals = set()
    for this_pandigital in itertools.permutations(digits, 10):
        if this_pandigital[5] not in (0, 5):
            continue
        if this_pandigital[3] not in (0, 2, 4, 6, 8):
            continue
        if (this_pandigital[2] + this_pandigital[3] + this_pandigital[4]) % 3 != 0:
            continue
        if (100 * this_pandigital[4] + 10 * this_pandigital[5] + this_pandigital[6]) % 7 != 0:
            continue
        if (100 * this_pandigital[5] + 10 * this_pandigital[6] + this_pandigital[7]) % 11 != 0:
            continue
        if (100 * this_pandigital[6] + 10 * this_pandigital[7] + this_pandigital[8]) % 13 != 0:
            continue
        if (100 * this_pandigital[7] + 10 * this_pandigital[8] + this_pandigital[9]) % 17 != 0:
            continue
        pandigital_totals.add(1000000000 * this_pandigital[0] + 100000000 * this_pandigital[1] +
                              10000000 * this_pandigital[2] + 1000000 * this_pandigital[3] +
                              100000 * this_pandigital[4] + 10000 * this_pandigital[5] + 1000 * this_pandigital[6] +
                              100 * this_pandigital[7] + 10 * this_pandigital[8] + this_pandigital[9])
    print(pandigital_totals)
    print(sum(pandigital_totals))


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
