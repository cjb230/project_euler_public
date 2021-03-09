import datetime
import functools
import math

ALL_PENTAGONALS = {1: 1, 2: 5}


@functools.lru_cache(maxsize=None)
def pentagonal(n):
    global ALL_PENTAGONALS
    try:
        result = ALL_PENTAGONALS[n]
    except KeyError:
        result = int(n * ((3*n) - 1) / 2)
        ALL_PENTAGONALS[n] = result
    return result


@functools.lru_cache(maxsize=None)
def is_pentagonal(n):
    global ALL_PENTAGONALS
    max_known = max(ALL_PENTAGONALS.values())
    if max_known < n:
        next_val = max(ALL_PENTAGONALS.keys()) + 1
        while n < max(ALL_PENTAGONALS.values()):
            ALL_PENTAGONALS[next_val] = int(n * ((3 * n) - 1) / 2)
            next_val += 1
    if n == max_known:
        return True
    else:
        if n in ALL_PENTAGONALS.values():
            return True
        else:
            return False


def main():
    subscript_total = 3
    not_found = True
    while not_found:
        small_subscript = 1
        big_subscript = subscript_total - 1
        while small_subscript <= big_subscript:
            sum = pentagonal(small_subscript) + pentagonal(big_subscript)
            if is_pentagonal(sum):
                diff = pentagonal(big_subscript) - pentagonal(small_subscript)
                if is_pentagonal(diff):
                    print(subscript_total, small_subscript, big_subscript, sum, diff)
                    print("Done")
                    not_found = False
                    break
                #print(subscript_total, small_subscript, big_subscript, sum)

            small_subscript += 1
            big_subscript -= 1
        subscript_total += 1

        if subscript_total % 10 == 0:
            print(subscript_total)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
