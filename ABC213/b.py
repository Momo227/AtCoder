def main():
    n = int(input())

    a = list(map(int, input().split()))
    b = sorted(a)[-2]
    c = a.index(b)
    c = int(c)
    print(a.index(b) + 1)

if __name__ == '__main__':
    main()