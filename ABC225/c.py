def main():
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]

    # 縦
    for i in range(n-1):
        if b[i+1][0] - b[i][0] != 7:
            print("No")
            exit()

    # 横
    for i in range(n):
        for j in range(m - 1):
            if b[i][j + 1] - b[i][j] != 1:
                print("No")
                exit()

    for j in range(m-1):
        if( b[0][j+1] - 1 ) % 7 <= ( b[0][j] - 1 ) % 7:
            print("No")
            exit()


    print("Yes")

if __name__ == '__main__':
    main()