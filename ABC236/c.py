from collections import defaultdict

def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()

    ans = defaultdict(int)
    for i in range(len(s)):
        ans[s[i]] += 1

    for i in range(len(t)):
        ans[t[i]] += 1

    for k, v in ans.items():
        if v == 1:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    main()