def main():
    n = int(input())

    a = list(map(int, input().split()))

    a = sorted(a)


    for i in range(n):
        if a[i] != i+1:
            print("No")
            exit()


    print("Yes")



if __name__ == '__main__':
    main()