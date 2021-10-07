def main():

    a, b = list(map(int, input().split()))

    # a = int(bin(a))
    # b = int(bin(b))

    # c = a^b
    c = bin(a ^ b)

    c = int(c, base=2)

    print(c)

if __name__ == '__main__':
    main()