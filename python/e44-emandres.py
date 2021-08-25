import datetime
from math import sqrt


def pent(x):
    return x*(3*x-1)/2


def is_pent(x):
    f = (.5 + sqrt(.25+6*x))/3
    if f - int(f) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    start = datetime.datetime.now()
    flag = False
    for i in range(1,3000):
        if i % 100 == 0:
            print('i = %d' % i)
        for j in range(i+1,3000):
            if is_pent(pent(j) - pent(i)) and is_pent(pent(j) + pent(i)):
                print('answer = %d' % (pent(j) - pent(i)))
                flag = True
                break
        if flag:
            break
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
