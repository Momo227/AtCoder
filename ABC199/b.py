def main():

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cnt = 0

    for i in range(1, 1001):
        ok = True
        for j in range(n):
            if i < a[j] or i > b[j] : ok = False
        if ok : cnt += 1

    print(cnt)





if __name__ == '__main__':
    main()