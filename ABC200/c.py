import itertools

def main():
    cnt = int(input())
    num = list(map(int, input().split()))
    ans = 0
    odd = []
    even = []
    cnt1 = 0
    cnt2 = 0

    for i in range(cnt):
        if num[i]%2:
            odd.append(num[i])
            cnt1 += 1
        else:
            even.append(num[i])
            cnt2 += 1

    for i in range(cnt1):
        for j in range(i):
            if i > j:
                sub = odd[i] - odd[j]
                if sub % 200 == 0:
                    ans += 1

    for i in range(cnt2):
        for j in range(i):
            if i > j:
                sub = even[i] - even[j]
                if sub % 200 == 0:
                    ans += 1


    print(ans)
if __name__ == '__main__':
    main()