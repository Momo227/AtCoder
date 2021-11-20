
def main():
    n, k = map(int, input().split())
    a = [sum(list(map(int, input().split()))) for _ in range(n)]

    # 基準となる点数
    b = sorted(a, reverse=True)[k - 1];
    for x in a:
        print("Yes" if x + 300 >= b else "No")


if __name__ == '__main__':
    main()