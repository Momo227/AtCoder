def main():
    n1, n2 = list(map(int, input().split()))

    if (n1*n2)%2 == 0:
        print('Even')
    else:
        print('Odd')


if __name__ == '__main__':
    main()