def main():

    n = int(input())
    s = input()
    q = int(input())

    list = []
    moji = ','.join(map(lambda x: '"{}"'.format(x), list(s)))

    for i in range(q):
        t, a, b = input().split()
        t = int(t)
        a = int(a)
        b = int(b)

        if(t==1):
            k = moji[a]
            moji[a] = moji[b]
            moji[b] = k
        elif(t==2):
            for j in range(n):
                e = moji[j]
                moji[j] = moji[-n+j]
                moji[j] = e



        list.append([t, a, b])

    print(s[1])



    # print(n, s, q)
    #
    # print(list)



if __name__ == '__main__':
    main()