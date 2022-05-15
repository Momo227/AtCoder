def main():
    s = list(input())

    num = len(s)

    ans = []

    if num == 1:
        for i in range(6):
            for j in range(len(s)):
                ans.append(s[j])
    elif num == 2:
        for i in range(3):
            for j in range(len(s)):
                ans.append(s[j])
    else:
        for i in range(2):
            for j in range(len(s)):
                ans.append(s[j])

    print("".join(ans))


if __name__ == '__main__':
    main()
