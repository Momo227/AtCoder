def main():
    n = int(input())
    a = list(map(int, input().split()))

    a = set(a)
    for i in range(2001):
        if i not in a:
            print(i)
            exit()


if __name__ == '__main__':
    main()
