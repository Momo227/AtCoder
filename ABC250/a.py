def main():
    h, w = list(map(int, input().split()))
    r, c = list(map(int, input().split()))

    ans = 0

    if r + 1 <= h:
        ans += 1
    if r - 1 > 0:
        ans += 1
    if c + 1 <= w:
        ans += 1
    if c - 1 > 0:
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
