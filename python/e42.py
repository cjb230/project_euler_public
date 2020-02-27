import datetime

SOURCE_FILE = 'p042_words.txt'
ALL_WORD_VALUES = dict()
TRIANGLE_NUMBERS = list()


def triangle(n):
    return int(0.5 * n * (n + 1))


def main():
    with open(SOURCE_FILE) as f:
        file = f.read()
    words = file.replace('"', '').split(',')

    max_word_value = 0
    for word in words:
        word_value = 0
        for letter in word:
            word_value += ord(letter) - 64
        if word_value > max_word_value:
            max_word_value = word_value
        if word_value in ALL_WORD_VALUES:
            ALL_WORD_VALUES[word_value] = ALL_WORD_VALUES[word_value] + 1
        else:
            ALL_WORD_VALUES[word_value] = 1

    n = 1
    while True:
        triangle_n = triangle(n)
        TRIANGLE_NUMBERS.append(triangle_n)
        if triangle_n > max_word_value:
            break
        else:
            n += 1

    coded_words = 0
    for this_triangle in TRIANGLE_NUMBERS:
        if this_triangle in ALL_WORD_VALUES:
            coded_words += ALL_WORD_VALUES[this_triangle]

    print(coded_words)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
