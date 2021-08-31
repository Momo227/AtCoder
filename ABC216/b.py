def main():
    s = []
    t = []
    n = int(input())

    for i in range(n):
        a = input().split()
        s.append(a)

    for i in range(n):
        t.append(s[i][1])
        s[i] = s[i][0]

    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j] and t[i] == t[j]:
                print("Yes")
                exit()
            else:
                continue

    print("No")




if __name__ == '__main__':
    main()