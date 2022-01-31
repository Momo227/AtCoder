import sys

def main():
    l = []
    r = []
    N = int(input())
    S = input()
    for i, c in enumerate(S):
        if c == 'L':
            r.append(i)
        else:
            l.append(i)
    # Python ではアスタリスク * を使って List の内容を別個に取り出して、関数に渡すことができる。
    print(*(l + [N] + r[::-1]))


if __name__ == '__main__':
    main()
