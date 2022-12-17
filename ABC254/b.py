import math


def main():
    n = int(input())
    for row in range(1, n + 1):
        for k in range(1, row + 1):
            n = row - 1
            k = k - 1
            res = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
            print(res, end=' ')
        print()


if __name__ == '__main__':
    main()
