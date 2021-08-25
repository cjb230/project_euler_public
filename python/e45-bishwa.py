import datetime


def main():
    pentagonal_n = 1
    hexagonal_n = 1
    current_pentagonal_number = 1
    current_hexagonal_number = 1

    while True:
        if current_pentagonal_number == current_hexagonal_number:
            if current_pentagonal_number > 40755:
                print('Pentagonal ' + str(pentagonal_n) + ' = ' + str(current_pentagonal_number))
                print('Hexagonal ' + str(hexagonal_n) + ' = ' + str(current_hexagonal_number))
                break
            else:
                pentagonal_n += 1
                current_pentagonal_number = int(pentagonal_n * ((3 * pentagonal_n) - 1) / 2)
        elif current_hexagonal_number > current_pentagonal_number:
            pentagonal_n += 1
            current_pentagonal_number = int(pentagonal_n * ((3 * pentagonal_n) - 1) / 2)
        elif current_hexagonal_number < current_pentagonal_number:
            hexagonal_n += 1
            current_hexagonal_number =  hexagonal_n * ((2 * hexagonal_n) - 1)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print()
    print(str(duration.total_seconds()) + " seconds")
