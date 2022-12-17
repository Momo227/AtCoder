def main():
    n = int(input())
    s = list(input())

    double = False

    for i in range(n):
        if s[i] == '"' and double == False:
            double = True
        elif s[i] == '"' and double == True:
            double = False
        elif s[i] == "," and double == False:
            s[i] = "."
        else:
            continue

    print("".join(s))


if __name__ == '__main__':
    main()
