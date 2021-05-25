def main():
    a, b, c = list(map(int, input().split()))

    if (a > b):
        d = a
        a = b
        b = d
    if (b > c):
        d = b
        b = c
        c = d
    if (a > b):
        d = a
        a = b
        b = d

    if (c - b) == (b - a):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()