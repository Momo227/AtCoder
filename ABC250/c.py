from collections import defaultdict


def main():
    n, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    ans = [i + 1 for i in range(n)]
    index = defaultdict(int)

    for i in range(n):
        index[i + 1] = i

    for i in range(q):
        target = a[i]
        idx = index[target]
        to_idx = idx + 1
        if index == n - 1:
            to_idx = idx - 1

        tmp = ans[to_idx]
        ans[to_idx] = ans[idx]
        ans[idx] = tmp
        index[ans[to_idx]] = to_idx
        index[ans[idx]] = idx

    for i in range(n):
        print(ans[i])


if __name__ == '__main__':
    main()
