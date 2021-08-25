import datetime
import math


def main():
    for denominator in range(11, 100):
        denominator_tens = math.floor(denominator / 10)
        denominator_units = denominator % 10
        if denominator % 10 == 0:
            denom_ends_with_zero = True
        else:
            denom_ends_with_zero = False
        for numerator in range(10, denominator):
            numerator_tens = math.floor(numerator / 10)
            numerator_units = numerator % 10
            correct_result = numerator / denominator
            if denom_ends_with_zero is False or numerator % 10 != 0:
                if numerator_units == denominator_tens and denominator_units != 0:
                    if numerator_tens / denominator_units == correct_result:
                        print("FOUND: (", numerator_tens, "/", denominator_units, ") = (", numerator, "/", denominator, ")")
                if numerator_tens == denominator_units:
                    if numerator_units / denominator_tens == correct_result:
                        print("FOUND: (", numerator_units, "/", denominator_tens, ") = (", numerator, "/", denominator, ")")


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
