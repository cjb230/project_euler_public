import datetime


def digit_sum(number_in):
    total = 0
    for this_digit in str(number_in):
        total += int(this_digit)
    return total


def main():
    max_sum = 0
    max_a = 0
    max_b = 0
    for a in range(1, 100):
        intermediate_result = 1
        for b in range(1, 100):
            intermediate_result *= a
            this_sum = digit_sum(intermediate_result)
            if this_sum > max_sum:
                max_sum = this_sum
                max_a = a
                max_b = b
    print(max_sum)
    print(max_a)
    print(max_b)
    print(pow(max_a, max_b))


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
