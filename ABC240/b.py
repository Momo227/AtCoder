
def main():
    n = int(input())
    a = list(map(int, input().split()))

    a = set(a)

    print(len(a))

if __name__ == '__main__':
    main()
