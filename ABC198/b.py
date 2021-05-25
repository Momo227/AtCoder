def main():

    a = input()

    for i in range(10):
        b = "0"*i + a
        if(b == b[::-1]):
            print("Yes")
            exit()

    print("No")

if __name__ == '__main__':
    main()