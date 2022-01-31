def main():
    n = int(input())

    if n < (-2)**31 or n >= 2**31:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()