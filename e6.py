def main():
    running_sum = 0
    running_square_sum = 0

    for i in range(1, 101):
        running_sum += i
        running_square_sum += i ** 2

    print("Running sum square = " + str(5050 ** 2))
    print("Running square sum = " + str(running_square_sum))
    print("Difference = " + str(5050 ** 2 - running_square_sum))


if __name__ == "__main__":
    main()
