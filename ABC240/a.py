def main():
    a, b = list(map(int, input().split()))


    if a == 1:
        if b == 2 or b == 10:
            print("Yes")
            exit()
        else:
            print("No")
            exit()
    else:
        if b == a + 1:
            print("Yes")
            exit()

    print("No")


if __name__ == '__main__':
    main()