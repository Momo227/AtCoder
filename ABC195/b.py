def main():
    m, h = list(map(int, input().split()))

    if(h % m):
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    main()