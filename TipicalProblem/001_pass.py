import itertools

def check(center, sabun, split_num):
    count = 0
    now_long = 0
    for i in range(len(sabun)):
        now_long += sabun[i]
        if now_long >= center:
            count += 1
            now_long = 0
    if count >= split_num:
        return True
    else:
        return False


def main():
    n, l=list(map(int, input().split()))
    k = int(input())
    a = [0] +  list(map(int, input().split())) + [l]
    sabun = [a[i] - a[i - 1] for i in range(1, n + 2)]

    left, right = 0, l

    while 1:
        center = (right + left) // 2
        if check(center, sabun, k + 1):
            left = center
        else:
            right = center
        if right - left <= 1:
            break
    print(left)



if __name__ == '__main__':
    main()