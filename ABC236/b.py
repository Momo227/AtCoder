from collections import defaultdict
def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = defaultdict(int)
    for i in range(len(a)):
        ans[a[i]] += 1

    print([k for k, v in ans.items() if v == 3][0])


if __name__ == '__main__':
    main()