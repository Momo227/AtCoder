def main():
    n, m = list(map(int, input().split()))
    s = []
    for i in range(n):
        s.append(list(input()))

    for i in range(n):
        for j in range(m):
            if s[i][j] == "o":
                s[i][j] = 1
            else:
                s[i][j] = 0

    cnt = 0
    if n != 2:
        for i in range(n):
            for j in range(i + 1, n):
                combined1 = [x + y for (x, y) in zip(s[i], s[j])]
                if 0 in combined1:
                    continue
                else:
                    cnt += 1
    else:
        combined1 = [x + y for (x, y) in zip(s[0], s[1])]
        if 0 not in combined1:
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
