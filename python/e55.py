import datetime


def reverse_and_add(input):
    return input + int(str(input)[::-1])


def is_palindrome(test_num):
    if str(test_num) == str(test_num)[::-1]:
        return True
    return False


def main():
    total = 0
    for x in range(1, 10000):
        #print(x)
        is_potential_lychrel = True
        test_num = reverse_and_add(x)
        iters = 1
        while iters <= 50 and is_potential_lychrel is True:
            if is_palindrome(test_num):
                is_potential_lychrel = False
                #print('Palindrome found:', test_num)
            else:
                test_num = reverse_and_add(test_num)
            #print(" " * iters, test_num)
            iters += 1
        if is_potential_lychrel:
            total += 1
        #print('Total checked:', x, '  "Lychrel" found:', total)
        #print()
    print(total)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
