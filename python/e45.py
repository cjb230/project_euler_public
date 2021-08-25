import datetime
import math


def is_hexagonal(test_number):
    low_test_bound = math.floor(math.sqrt(test_number / 2)) - 1
    next_test = low_test_bound
    result = False

    while True:
        test_result = next_test * ((2 * next_test) - 1)
        if test_result == test_number:
            result = next_test
            break
        elif test_result > test_number:
            break
        else:
            next_test += 1

    if test_number == 40755:
        result = False
    return result


def main():
    triangular_n = 1
    pentagonal_n = 1
    current_triangular_number = 1
    current_pentagonal_number = 1

    while True:
        if current_triangular_number == current_pentagonal_number:
            hex_result = is_hexagonal(current_triangular_number)
            if hex_result and triangular_n > 1:
                print('Triangular ' + str(triangular_n) + ' = ' + str(current_triangular_number))
                print('Pentagonal ' + str(pentagonal_n) + ' = ' + str(current_pentagonal_number))
                print('Hexagonal ' + str(hex_result) + ' = ' + str(current_pentagonal_number))
                break
            else:
                triangular_n += 1
                current_triangular_number = int(triangular_n * (triangular_n + 1) / 2)
        elif current_triangular_number > current_pentagonal_number:
            pentagonal_n += 1
            current_pentagonal_number = int(pentagonal_n * ((3 * pentagonal_n) - 1) / 2)
        elif current_triangular_number < current_pentagonal_number:
            triangular_n += 1
            current_triangular_number =  int(triangular_n * (triangular_n + 1) / 2)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print()
    print(str(duration.total_seconds()) + " seconds")
