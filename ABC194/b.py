def main():
    n = int(input())

    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)

    i = a.index(min(a))
    j = b.index(min(b))

    # print(i, j)

    if i == j:
        c, d = a[i], b[j]
        del a[i]
        del b[j]
        ans = min(c+d, max(min(a), d), max(c, min(b)))

    else:
        ans = max(a[i], b[j])

    print(ans)



if __name__ == '__main__':
    main()