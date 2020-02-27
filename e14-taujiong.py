import datetime
# adapted from another result on forum, not my own. Combining dictionary look up with calculation, and using a dict,
# makes the whole thing much faster (approx 40s to approx 2s)

box = {1: 1}
result = 0
max = 0


def Collatz(num):
    global box
    if num in box.keys():
        return box[num]
    elif num % 2 == 0:
        step = Collatz(num / 2) + 1
    else:
        step = Collatz((3 * num + 1) / 2) + 2 # the div by 2 skips a call to this routine
    box[num] = step
    return step


def main():
    global result
    global max
    for i in range(1, 1000001):
        step = Collatz(i)
        if step > max:
            result = i
            max = step


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    print(result)
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
