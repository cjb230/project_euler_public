import datetime


def main():
    cumulative_length = 0
    cumulative_string = ''
    i = 1

    while True:
        this_string = str(i)
        this_string_len = len(this_string)
        cumulative_string += this_string
        cumulative_length += this_string_len

        if cumulative_length > 1000000:
            break

        i += 1

    result = int(cumulative_string[0]) * int(cumulative_string[9]) * int(cumulative_string[99]) * \
             int(cumulative_string[999]) * int(cumulative_string[9999]) * int(cumulative_string[99999]) *\
             int(cumulative_string[999999])

    print(result)

if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
