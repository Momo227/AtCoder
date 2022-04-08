def main():
    a, b, c, d = list(map(int, input().split()))

    if a < c:
        print("Takahashi")
        exit()
    elif a == c:
        if b <= d:
            print("Takahashi")
            exit()
        else:
            print("Aoki")
            exit()
    else:
        print("Aoki")


if __name__ == '__main__':
    main()
