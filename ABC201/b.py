def main():
    mylist = []
    N = int(input())

    # make list
    for i in range(N):
        a, b = input().split()
        b = int(b)
        mylist.append([a,b])

    items_sorted = sorted(mylist, reverse=True, key=lambda x: x[1])

    dic3 = items_sorted[1]
    print(dic3[0])



if __name__ == '__main__':
    main()