import math
def main():
    n = int(input())

    a = list(map(int, input().split()))
    # print(a)

    p = sum(a) ** 2
    # print(p)
    t = 0

    for i in a:
        # print(i)
        t += i ** 2
        # print(t)

    print(n * t - p)



if __name__ == '__main__':
    main()