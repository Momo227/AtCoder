def main():
    n, x = input().split()

    # 完全２分木→2進数
    x = list(bin(int(x)))
    for c in input():
        if c == 'U': x.pop()
        if c == 'L': x.append("0")
        if c == 'R': x.append("1")

    # 2がなければ10進数
    print(int("".join(x), 2))

if __name__ == '__main__':
    main()
