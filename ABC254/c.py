from collections import defaultdict

def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    ans = sorted(a)

    ind = defaultdict(list)

    for i in range(n):
        num = ind[ans[i]]
        index = i

        ind[ans[i]] = num

    for i in range(n - k):
        if a == ans:
            print("Yes")
            exit()
        sample = a[i]
        a[i] = a[i + k]
        a[i + k] = sample

    print("No")


if __name__ == '__main__':
    main()
