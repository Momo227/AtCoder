from collections import defaultdict
from math import factorial


def main():
    n = int(input())
    a = list(map(int, input().split()))

    suuzi = defaultdict(list)

    for i in range(n):
        index = suuzi[a[i]]
        index.append(i + 1)
        suuzi[a[i]] = index

    nagasa = []

    for k, v in suuzi.items():
        nagasa.append(len(v))

    print(nagasa)

    a = factorial(len(nagasa)) / factorial(3) / factorial(len(nagasa) - 3)

    for i in range(len(nagasa)):
        a *= nagasa[i]

    print(int(a))


if __name__ == '__main__':
    main()
