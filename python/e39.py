import datetime
import math


def solutions_for_perimeter(perimeter):
    # assume side lengths lengths a > b >= c
    # a is the length of the hypotenuse, if there is a solution
    solutions = 0
    max_hypotenuse_length = math.floor(perimeter / 2)
    min_hypotenuse_length = math.ceil(perimeter * (math.sqrt(2) / (2 + math.sqrt(2))))
    for a in range(min_hypotenuse_length, max_hypotenuse_length + 1):
        min_c = max(1, perimeter - (2 * a) + 1)
        max_c = math.floor((perimeter - a) / 2)
        for c in range(min_c, max_c + 1):
            b = perimeter - a - c
            if a * a == b * b + c * c:
                solutions += 1
                break
    return solutions


def main():
    max_solutions = 0
    max_solutions_perimeter = 0
    for perimeter in range(1, 1001):
        perimeter_solutions = solutions_for_perimeter(perimeter)
        if perimeter_solutions > max_solutions:
            max_solutions = perimeter_solutions
            max_solutions_perimeter = perimeter
    print('Perimeter with max solutions = ' + str(max_solutions_perimeter) + ', solutions = ' + str(max_solutions))


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
