def main():
    n, k = list(map(int, input().split()))

    for i in range(k):
        if (n%200==0):
            n = int(n/200)
        else:
            n = str(n) + '200'
            n = int(n)

    print(n)

if __name__ == '__main__':
    main()