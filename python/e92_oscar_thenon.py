import datetime


SQUARES = {'0': 0, '1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}


def chain_next(i):
    global SQUARES
    result = 0
    i_string = str(i)
    for digit in i_string:
        result += SQUARES[digit]
    return result


def main():
    set_1 = {44, 32, 13, 10, 1}
    set_89 = {85, 89, 145, 42, 20, 4, 16, 37, 58}

    for i in range(2, 10000001):
        if i in set_1:
            continue
        if i in set_89:
            continue
        this_chain = {i}
        next_chain = chain_next(i)
        while True:
            if next_chain not in set_1:
                if next_chain not in set_89:
                    this_chain.add(next_chain)
                    next_chain = chain_next(next_chain)
                else:
                    set_89.update(this_chain)
                    break
            else:
                set_1.update(this_chain)
                break

    print(len(set_89))


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
