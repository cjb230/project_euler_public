import datetime
import itertools


def main():
    digits = list(range(1, 10))
    pandigital_totals = set()
    for this_pandigital in itertools.permutations(digits, 9):
        a = 10 * this_pandigital[0] + this_pandigital[1]
        b = 100 * this_pandigital[2] + 10 * this_pandigital[3] + this_pandigital[4]
        c = 1000 * this_pandigital[5] + 100 * this_pandigital[6] + 10 * this_pandigital[7] + this_pandigital[8]
        if a * b == c:
            pandigital_totals.add(c)
        else:
            a = this_pandigital[0]
            b = 1000 * this_pandigital[1] + 100 * this_pandigital[2] + 10 * this_pandigital[3] + this_pandigital[4]
            if a * b == c:
                pandigital_totals.add(c)
    print(pandigital_totals)
    print(sum(pandigital_totals))


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
