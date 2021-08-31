def main():
    n = int(input())
    ans = []
    while(1):
        if n == 0:
            ans = ans[::-1]
            ans = ''.join(ans)
            print(ans)
            exit()
        elif n % 2 == 0:
            ans.append("B")
            n = n // 2
        else:
            ans.append("A")
            n = n - 1



if __name__ == '__main__':
    main()