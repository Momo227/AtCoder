def main():
    s = input()

    new_text = s.replace('6', 'a').replace('9', '6').replace('a', '9')

    ans = new_text[::-1]
    print(ans)


if __name__ == '__main__':
    main()