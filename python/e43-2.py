import datetime


def main():
    digits = [str(x) for x in list(range(0, 10))]
    m17 = [f'{x:03}' for x in range(0, 1001, 17) if len({f'{x:03}'[0], f'{x:03}'[1], f'{x:03}'[2]}) == 3]
    m13 = [f'{x:03}' for x in range(0, 1001, 13) if len({f'{x:03}'[0], f'{x:03}'[1], f'{x:03}'[2]}) == 3]
    m11 = [f'{x:03}' for x in range(0, 1001, 11) if len({f'{x:03}'[0], f'{x:03}'[1], f'{x:03}'[2]}) == 3]
    m7 = [f'{x:03}' for x in range(0, 1001, 7) if len({f'{x:03}'[0], f'{x:03}'[1], f'{x:03}'[2]}) == 3]
    m5 = [f'{x:03}' for x in range(0, 1001, 5) if len({f'{x:03}'[0], f'{x:03}'[1], f'{x:03}'[2]}) == 3]
    m3 = [f'{x:03}' for x in range(0, 1001, 3) if len({f'{x:03}'[0], f'{x:03}'[1], f'{x:03}'[2]}) == 3]
    m2 = [f'{x:03}' for x in range(0, 1001, 2) if len({f'{x:03}'[0], f'{x:03}'[1], f'{x:03}'[2]}) == 3]

    answer = 0
    for this_17 in m17:
        trial_digits_17 = digits.copy()
        trial_digits_17.remove(this_17[0])
        trial_digits_17.remove(this_17[1])
        trial_digits_17.remove(this_17[2])
        for this_13 in m13:
            if this_13[0] not in trial_digits_17:
                continue
            if this_13[1] == this_17[0] and this_13[2] == this_17[1]:
                trial_digits_13 = trial_digits_17.copy()
                trial_digits_13.remove(this_13[0])
                for this_11 in m11:
                    if this_11[0] not in trial_digits_13 or this_11[0] not in ('0', '5'):
                        continue
                    if this_11[1] == this_13[0] and this_11[2] == this_13[1]:
                        trial_digits_11 = trial_digits_13.copy()
                        trial_digits_11.remove(this_11[0])
                        for this_7 in m7:
                            if this_7[0] not in trial_digits_11:
                                continue
                            if this_7[1] == this_11[0] and this_7[2] == this_11[1]:
                                trial_digits_7 = trial_digits_11.copy()
                                trial_digits_7.remove(this_7[0])
                                for this_5 in m5:
                                    if this_5[0] not in trial_digits_7:
                                        continue
                                    if this_5[1] == this_7[0] and this_5[2] == this_7[1]:
                                        trial_digits_5 = trial_digits_7.copy()
                                        trial_digits_5.remove(this_5[0])
                                        for this_3 in m3:
                                            if this_3[0] not in trial_digits_5:
                                                continue
                                            if this_3[1] == this_5[0] and this_3[2] == this_5[1]:
                                                trial_digits_3 = trial_digits_5.copy()
                                                trial_digits_3.remove(this_3[0])
                                                for this_2 in m2:
                                                    if this_2[0] not in trial_digits_3:
                                                        continue
                                                    if this_2[1] == this_3[0] and this_2[2] == this_3[1]:
                                                        trial_digits_2 = trial_digits_3.copy()
                                                        trial_digits_2.remove(this_2[0])
                                                        answer += 1000000000 * int(trial_digits_2[0]) + 100000000 * \
                                                            int(this_2[0]) + 10000000 * int(this_3[0]) + 1000000 * \
                                                            int(this_5[0]) + 100000 * int(this_7[0]) + 10000 * \
                                                            int(this_11[0]) + 1000 * int(this_13[0]) + 100 * \
                                                            int(this_17[0]) + 10 * int(this_17[1]) + int(this_17[2])
                                                        print(trial_digits_2[0] + this_2[0] + this_3[0] + this_5[0] + this_7[0] + this_11[0] + this_13[0] + this_17)
    print(answer)


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    duration = end - start
    print(str(duration.total_seconds()) + " seconds")
