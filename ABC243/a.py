def main():
    v, a, b, c = list(map(int, input().split()))

    nokori = v

    while nokori > 0:
        nokori = nokori - a

        if nokori < 0:
            print("F")
            exit()
        if nokori == 0:
            print("M")
            exit()

        nokori = nokori - b

        if nokori < 0:
            print("M")
            exit()
        if nokori == 0:
            print("T")
            exit()

        nokori = nokori - c

        if nokori < 0:
            print("T")
            exit()
        if nokori == 0:
            print("F")
            exit()


if __name__ == '__main__':
    main()
