from collections import defaultdict


def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    # x, y = [list(i) for i in zip(*xy)]
    s = list(input())

    # print(xy)
    #
    ans = defaultdict(list)
    for i in range(n):
        ans[xy[i][1]].append([xy[i][0], s[i]])

    # print(ans)

    for k, v in ans.items():
        v.sort(key=lambda x: x[0])
        flag = False
        for i in range(len(v)):
            d = v[i][1]
            if not flag and d == "R":
                flag = True
            if flag and d == "L":
                print("Yes")
                exit()

    print("No")


if __name__ == '__main__':
    main()
