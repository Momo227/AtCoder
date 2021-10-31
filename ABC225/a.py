def main():
    s = list(input())

    s = sorted(s)

    if (s[0] == s[1]) and (s[0] == s[2]):
        print(1)
    elif (s[0] == s[1]) or (s[0] == s[2]) or (s[1] == s[2]) :
        print(3)
    else:
        print(6)



if __name__ == '__main__':
    main()