if __name__ == '__main__':
    # 神の数列
    import random
    a = int(input())
    b = int(input())

    a_seq = []
    b_seq = []

    sum = 0
    for k in range(a):
        x = random.randint(1, 1000)
        a_seq.append(x)
        sum = sum + x

    cnt = 0
    for k in range(b-1):
        b_seq.append(((-1)*k)-1)
        cnt = cnt + (((-1)*k)-1)

    b_seq.append(((-1)*sum + cnt))

    ans_seq = a_seq + b_seq
    print(ans_seq)
