import datetime


def main():
    for d in range(2, 1001):
        print(str(d), " ", str(1/d))


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
