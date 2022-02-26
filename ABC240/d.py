def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = []
    for i in range(n):
        ans.append(a[i])
        if ans[-a[i]:].count(a[i]) == a[i]:
            ans = ans[:-a[i]]
        print(len(ans))


if __name__ == '__main__':
    main()
