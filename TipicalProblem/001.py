import itertools

def main():
    n, l=list(map(int, input().split()))
    k = int(input())
    a = list(map(int, input().split()))
    c_list = list(itertools.combinations(list(range(n)),k))
    # print(c_list)
    # print(a)
    ans = 0

    for c_pair in c_list:
        # print(c_pair)
        c_pair_ans = 10**10

        for i in range(len(c_pair)):
            if i == 0:
                c_pair_ans = min(c_pair_ans, a[c_pair[i]])
            else:
                c_pair_ans = min(c_pair_ans, a[c_pair[i]] - a[c_pair[i-1]])
        c_pair_ans = min(c_pair_ans, l - a[c_pair[-1]])
        ans = max(ans, c_pair_ans)
        # print(c_pair_ans, ans)

    print(ans)




if __name__ == '__main__':
    main()