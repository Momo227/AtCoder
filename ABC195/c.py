import math
def main():
    a, b ,w = list(map(int, input().split()))

    w = 1000*w
    max = math.floor(w/a)
    min = math.ceil(w/b)

    # print(max, min)


    if (max < min):
        print("UNSATISFIABLE")
    else:
        print(min, max)



if __name__ == '__main__':
    main()