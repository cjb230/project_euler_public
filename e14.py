import datetime


def calculate_collatz_length(input_number):
    next_step = input_number
    steps_to_one = 1
    while next_step > 1:
        steps_to_one += 1
        if next_step % 2 == 0:
            next_step /= 2
        else:
            next_step = (3 * next_step) + 1
    return steps_to_one


def main():
    max_steps = 1
    max_steps_start = 0
    for i in range(1, 1000001):
        this_collatz_length = calculate_collatz_length(i)
        if this_collatz_length > max_steps:
            max_steps = this_collatz_length
            max_steps_start = i
    print("i: " + str(max_steps_start), " steps: " + str(max_steps))


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
