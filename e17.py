import datetime

LETTERS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
           11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
           18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
           70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred"}


def sub_hundred_string(i):
    number_string = ""
    tens = i - (i % 10)
    units = (i % 10)
    if 1 <= i < 21:
        number_string = LETTERS[i]
    elif 21 <= i < 100:
        number_string = LETTERS[tens]
        if units != 0:
            number_string += LETTERS[units]
    return number_string


def main():
    total_chars = 0
    for i in range(1, 1001):
        number_string = ""
        hundreds = 0

        if i >= 100:
            hundreds = i - (i % 100)
            number_string = LETTERS[hundreds / 100] + "hundred"
        else:
            hundreds = 0
        units = (i % 10)
        tens = i - hundreds - units

        if hundreds > 0 and (tens + units) > 0:
            number_string += " and " + sub_hundred_string(i % 100)
        elif hundreds == 0 and (tens + units) > 0:
            number_string = sub_hundred_string(i % 100)

        if i == 1000:
            number_string = "one thousand"

        string_length = len(number_string)
        for c in number_string:
            if c == " ":
                string_length -= 1
        total_chars += string_length
    print(total_chars)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
