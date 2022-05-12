def main():
    n, a, b = list(map(int, input().split()))

    tail_1 = []
    tail_2 = []
    tail_1_mini = []
    tail_2_mini = []
    for j in range(b):
        tail_1_mini.append(".")
        tail_2_mini.append("#")
    tail_1.append("".join(tail_1_mini))
    tail_1.append("".join(tail_2_mini))
    tail_2.append("".join(tail_2_mini))
    tail_2.append("".join(tail_1_mini))

    tail_1 = "".join(tail_1)
    tail_2 = "".join(tail_2)

    sample_1 = []
    sample_2 = []
    ans = []

    if n % 2 == 0:
        for i in range(a):
            mini_sample = []
            for j in range(int(n / 2)):
                mini_sample.append(tail_1)
            sample_1.append("".join(mini_sample))
        for i in range(a):
            mini_sample = []
            for j in range(int(n / 2)):
                mini_sample.append(tail_2)
            sample_2.append("".join(mini_sample))

        for i in range(int(n / 2)):
            ans.append(sample_1)
            ans.append(sample_2)
    else:
        for i in range(a):
            mini_sample = []
            for j in range(int(n / 2)):
                mini_sample.append(tail_1)
            tail_1_mini = "".join(tail_1_mini)
            mini_sample.append(tail_1_mini)
            sample_1.append("".join(mini_sample))
        for i in range(a):
            mini_sample = []
            for j in range(int(n / 2)):
                mini_sample.append(tail_2)
            tail_2_mini = "".join(tail_2_mini)
            mini_sample.append(tail_2_mini)
            sample_2.append("".join(mini_sample))

        for i in range(int(n / 2)):
            ans.append(sample_1)
            ans.append(sample_2)
        ans.append(sample_1)

    for i in range(n):
        for j in range(len(ans[0])):
            print(ans[i][j])


if __name__ == '__main__':
    main()
