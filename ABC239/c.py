import math


def main():
    x1, y1, x2, y2 = list(map(int, input().split()))


    l = (x1 - x2) ** 2 + (y1 - y2) ** 2


    if l == 16 or l == 20 or l == 18 or l == 10 or l == 4 or l == 2:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
