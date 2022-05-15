from collections import defaultdict


def main():
    n = int(input())
    st = [input().split() for _ in range(n)]
    s, t = [list(i) for i in zip(*st)]

    for i in range(n):
        t[i] = int(t[i])

    ans = defaultdict(int)

    for i in range(n):
        if s[i] not in ans.keys():
            ans[s[i]] = t[i]

    s_max = ""
    t_max = 0
    for k, v in ans.items():
        if t_max < v:
            s_max = k
            t_max = v

    for i in range(n):
        if t[i] == t_max and s[i] == s_max:
            print(i + 1)
            exit()


if __name__ == '__main__':
    main()
