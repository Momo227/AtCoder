from numpy import poly1d
def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))



    # 多項式インスタンスの生成
    poly_a = poly1d(list(reversed(a)))
    poly_c = poly1d(list(reversed(c)))

    # Bを求める
    poly_b = poly_c / poly_a

    # Bの係数(.c:係数を取得)
    coefB = list(map(int, poly_b[0].c))

    # 順番を逆にして出力
    ans = list(reversed(coefB))
    print(*ans)


if __name__ == '__main__':
    main()
