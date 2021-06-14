def main():
    a, b, c = list(map(int, input().split()))

    if a >= 0 and b >=0:
        if a > b:
            print(">")
        if b > a:
            print("<")
        if a == b:
            print("=")

    elif a < 0 and b >=0:
        if c % 2 == 1:
            print("<")
        else:
            if abs(a) > abs(b):
                print(">")
            if abs(b) > abs(a):
                print("<")
            if abs(a) == abs(b):
                print("=")

    elif a >= 0 and b < 0:
        if c % 2 == 1:
            print(">")
        else:
            if abs(a) > abs(b):
                print(">")
            if abs(b) > abs(a):
                print("<")
            if abs(a) == abs(b):
                print("=")

    elif a < 0 and b < 0:
        if c % 2 == 1:
            if abs(a) > abs(b):
                print("<")
            if abs(b) > abs(a):
                print(">")
            if abs(a) == abs(b):
                print("=")
        else:
            if abs(a) > abs(b):
                print(">")
            if abs(b) > abs(a):
                print("<")
            if abs(a) == abs(b):
                print("=")


if __name__ == '__main__':
    main()