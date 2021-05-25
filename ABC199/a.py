def main():

    a, b, c = list(map(int, input().split()))

    d = a*a
    e = b*b
    f = c*c

    if(d+e<f):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()