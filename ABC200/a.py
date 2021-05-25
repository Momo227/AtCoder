def main():
    year = int(input())

    if year%100 == 0:
        print(int(year/100))
    else:
        print(int((year/100)+1))

if __name__ == '__main__':
    main()