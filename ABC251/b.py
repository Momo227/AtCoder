from itertools import combinations


def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))

    flag = [False for _ in range(w)]

    for i in range(n):
        if a[i] <= w:
            flag[a[i]] = True

    if len(a) >= 2:
        for i in range(n):
            for j in range(i + 1, n):
                s = a[i] + a[j]
                if s <= w:
                    flag[s] = True

    if len(a) >= 3:
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    s = a[i] + a[j] + a[k]
                    if s <= w:
                        flag[s] = True

    cnt = 0
    for i in range(w):
        if flag[i] == True:
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
