def main():
    h, w, n = map(int, input().split())
    ab = []
    a = []
    b = []

    for i in range(n):
        ab.append(list(map(int, input().split())))
        a.append([i, ab[i][0], 1])
        b.append([i, ab[i][1], 1])
    a.sort(key=lambda x: x[1])
    b.sort(key=lambda x: x[1])
    for i in range(1, n):
        if a[i - 1][1] == a[i][1]:
            a[i][2] = a[i - 1][2]
        else:
            a[i][2] = a[i - 1][2] + 1
    for i in range(1, n):
        if b[i - 1][1] == b[i][1]:
            b[i][2] = b[i - 1][2]
        else:
            b[i][2] = b[i - 1][2] + 1
    a.sort(key=lambda x: x[0])
    b.sort(key=lambda x: x[0])
    for i in range(n):
        print(str(a[i][2]) + " " + str(b[i][2]))
    h, w, n = map(int, input().split())
    ab = []
    a = []
    b = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
        a.append([i, ab[i][0], 1])
        b.append([i, ab[i][1], 1])
    a.sort(key=lambda x: x[1])
    b.sort(key=lambda x: x[1])
    for i in range(1, n):
        if a[i - 1][1] == a[i][1]:
            a[i][2] = a[i - 1][2]
        else:
            a[i][2] = a[i - 1][2] + 1
    for i in range(1, n):
        if b[i - 1][1] == b[i][1]:
            b[i][2] = b[i - 1][2]
        else:
            b[i][2] = b[i - 1][2] + 1
    a.sort(key=lambda x: x[0])
    b.sort(key=lambda x: x[0])
    for i in range(n):
        print(str(a[i][2]) + " " + str(b[i][2]))


if __name__ == '__main__':
    main()