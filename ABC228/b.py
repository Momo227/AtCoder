def main():

    n, x = map(int, input().split())
    friend = list(map(int, input().split()))


    know = []
    know.append(x)
    next = friend[x-1]
    for _ in range(n):
        know.append(next)
        nexts = next
        next = friend[nexts-1]

    know = set(know)
    print(len(know))



if __name__ == '__main__':
    main()