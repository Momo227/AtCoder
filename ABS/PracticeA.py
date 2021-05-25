def main():
    a = int(input())
    b, c = list(map(int, input().split()))
    s = input()

    d = int(a + b + c)

    print(d, s)

if __name__ == '__main__':
    main()