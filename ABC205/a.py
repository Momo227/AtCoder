def main():
    a, b = list(map(int, input().split()))

    if (a*(b/100) - int(a*(b/100)) == 0):
        print(int(a * (b / 100)))
    else:
        print(a*(b/100))

if __name__ == '__main__':
    main()