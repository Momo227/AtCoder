def main():
    cnt = 0
    number = list(map(int, input()))
    # print(number)

    for i in number:
        # print(i)
        if i:
            cnt+=1

    print(cnt)




if __name__ == '__main__':
    main()