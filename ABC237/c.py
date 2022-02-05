def main():
    s = input()
    if str(s) == "".join(reversed(s)):
        print("Yes")
        exit()

    s = list(s)
    cnt = 0
    cnt2 = 0
    for i in range(len(s)):
        if s[i] == "a":
            cnt += 1
        else:
            break

    s.reverse()
    for i in range(len(s)):
        if s[i] == "a":
            cnt2 += 1
        else:
            break

    s.reverse()
    s = "".join(s)
    s = "a" * (cnt2 - cnt) + s
    if str(s) == "".join(reversed(s)):
        print("Yes")
        exit()

    print("No")


if __name__ == '__main__':
    main()
