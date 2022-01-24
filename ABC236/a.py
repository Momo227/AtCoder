def main():
    s = list(input())
    a, b = list(map(int, input().split()))

    m = s[a-1]
    s[a-1] = s[b-1]
    s[b-1] = m

    print("".join(s))
if __name__ == '__main__':
    main()