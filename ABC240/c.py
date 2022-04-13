def main2():
    n, x = map(int, input().split())
    dp = 1

    for _ in range(n):
        # 読み込み
        a, b = map(int, input().split())
        # << : 左辺の値を右辺の値だけ左へシフト
        # | : 論理和
        dp = (dp << a) | (dp << b)

        # & : 論理積
    print("Yes" if ((dp >> x) & 1) == 1 else "No")


if __name__ == '__main__':
    main2()


def main():
    n, x = list(map(int, input().split()))

    ans = [False for _ in range(x + 1)]
    ans[0] = True
    for i in range(n):
        a, b = list(map(int, input().split()))
        mini = [False for _ in range(x + 1)]
        for j in range(x + 1):
            if not ans[j]:
                continue
            if j + a <= x:
                mini[j + a] = True
            if j + b <= x:
                mini[j + b] = True

        ans = mini

    if ans[x]:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
