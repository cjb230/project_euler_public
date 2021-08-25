import datetime


def main():
    candidate = 0
    continue_calculating = True
    while continue_calculating:
        candidate += 1
        candidate_x2 = candidate * 2
        candidate_string = sorted(str(candidate))
        if candidate_string == sorted(str(candidate_x2)):
            candidate_x3= candidate * 3
            if candidate_string == sorted(str(candidate_x3)):
                candidate_x4 = candidate * 4
                if candidate_string == sorted(str(candidate_x4)):
                    candidate_x5 = candidate * 5
                    if candidate_string == sorted(str(candidate_x5)):
                        candidate_x6 = candidate * 6
                        if candidate_string == sorted(str(candidate_x6)):
                            print(candidate)
                            print(candidate_x2)
                            print(candidate_x3)
                            print(candidate_x4)
                            print(candidate_x5)
                            print(candidate_x6)
                            continue_calculating = False
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
