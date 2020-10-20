import datetime


def main():
    highest_pandigital = ''
    for my_int in range(1, 10001):
        possible_pandigital = ''
        n = 1
        while len(possible_pandigital) < 9:
            possible_pandigital += str(n * my_int)
            if len(possible_pandigital) == 9 and '0' not in possible_pandigital:
                if len({possible_pandigital[x] for x in range(len(possible_pandigital))}) == 9:
                    if possible_pandigital > highest_pandigital:
                        highest_pandigital = possible_pandigital
                        print(possible_pandigital, ", n=", n, ", my_int= ", my_int)
            n += 1


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
