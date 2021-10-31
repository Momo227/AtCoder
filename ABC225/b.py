def main():

    n = int(input())
    a = []
    b = []
    for i in range(1, n):
        x, y = input().split()
        a.append(int(x))
        b.append(int(y))

    for i in range(1, n+1):
        cnt = 0
        for j in range(n-1):
            if (i == a[j]) or (i == b[j]):
                cnt += 1
                if cnt == n-1:
                    print("Yes")
                    exit()
            else:
                break

    print("No")






if __name__ == '__main__':
    main()