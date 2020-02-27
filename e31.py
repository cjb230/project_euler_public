import datetime

WAYS_OF_MAKING = dict.fromkeys(range(0, 6), None)
COINS = (1, 2, 5, 10, 20, 50, 100, 200)


def main():
    print(COINS)
    prev_coin = None
    for this_coin in COINS:
        for target, way_counts in WAYS_OF_MAKING.items():


        prev_coin = this_coin

    print(WAYS_OF_MAKING)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
