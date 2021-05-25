def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ls = [0 for _ in range(n + 1)]
    # ls = []
    # for i in range(n):
    #     ls.append(0)

    for i in range(n):
        score = b[c[i]-1]
        ls[score] += 1
        # print(ls)

    cnt = 0
    for i in range(n):
        score = a[i]
        cnt += ls[score]

    print(cnt)


if __name__ == '__main__':
    main()