from collections import defaultdict
import collections


def main():
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        if a[i] == b[i]:
            cnt += 1

    print(cnt)

    c = a + b
    d = collections.Counter(c)

    cnt2 = list(d.values())

    ans = 0
    for i in range(len(cnt2)):
        if cnt2[i] == 2:
            ans += 1

    print(ans - cnt)


if __name__ == '__main__':
    main()
