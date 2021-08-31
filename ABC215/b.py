def main():

    n = int(input())
    cnt = 0
    while(1):
        if n == 1:
            break
        n //= 2
        cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()