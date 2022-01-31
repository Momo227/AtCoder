import numpy as np

def main():
    h, w = map(int, input().split())

    a = [input().split() for l in range(h)]

    t = np.array(a)

    b = t.T.tolist()

    for i in range(w):
        print(" ".join(b[i]))

if __name__ == '__main__':
    main()

