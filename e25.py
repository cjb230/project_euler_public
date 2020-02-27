import datetime
import math

def main():
    i = 3
    a = 1
    b = 1
    while True:
        c = a + b
        if math.ceil(math.log10(c)) == 1000:
            print("i: " + str(i) + " f(i) = " + str(c))
            break
        a = b
        b = c
        i += 1


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")