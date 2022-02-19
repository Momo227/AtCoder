import sys

def main():

    a, b, c, d = list(map(int, input().split()))

    min = a + c
    max = b + d

    sa = b - a + 1

    sosuu = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
             97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

    kouho = [i for i in sosuu if i >= min and i <= max]

    mini = []
    for i in range(sa):
        flag = []
        num = a + i
        for n in kouho:
            ans = n - num
            if ans >= c and ans <= d:
                flag.append("p")
            else:
                flag.append("q")
        if str("p") in flag:
            mini.append("p")
        else:
            mini.append("q")

    if str("q") in mini:
        print("Takahashi")
    else:
        print("Aoki")



if __name__ == '__main__':
    main()
