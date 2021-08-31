def main():
    X = list(input())

    y = int(X[len(X)-1])

    ans = []

    for i in range(len(X)-2):
        ans.append(X[i])



    if 0 <= y and y <= 2:
        ans.append("-")
    elif 7 <= y and y <= 9:
        ans.append("+")

    kotae = ''.join(ans)
    print(kotae)



if __name__ == '__main__':
    main()