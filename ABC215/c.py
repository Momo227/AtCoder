import itertools

def main():
    s,k = input().split()
    s = list(s)
    k = int(k)
    s = sorted(s)

    ans = []
    for v in itertools.permutations(s, len(s)):
        ans.append(v)
    # print(ans)
    ans = set(ans)
    ans = list(ans)
    ans = sorted(ans)
    # print(ans)

    kotae = ''.join(ans[k-1])
    print(kotae)




if __name__ == '__main__':
    main()