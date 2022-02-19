
def main():
    n = int(input())

    if n >= 0:
        print(n//10)
    else:
        if n % 10 == 0:
            n = -n
            print(-(n//10))
        else:
            n = -n
            print(-(n // 10 + 1))

if __name__ == '__main__':
    main()
