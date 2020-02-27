def main():
    for c in range(997, 2, -1):
        for b in range(1000 - c - 1, 1, -1):
            a = 1000 - c - b
            if a ** 2 + b ** 2 == c ** 2:
                print(str(a) + " " + str(a ** 2))
                print(str(b) + " " + str(b ** 2))
                print(str(c) + " " + str(c ** 2))
                print("abc = " + str(a * b * c))
                return


if __name__ == "__main__":
    main()
