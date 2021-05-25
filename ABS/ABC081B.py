def division(cnt, nums):
    ans = 0

    for i in range(cnt):
        if nums[i] % 2 || nums[i] == 1:
            break
        else:
            nums[i] = nums[i] / 2
        ans += 1
        print(ans)
        i += 1
    return ans

def main():
    i = 0
    cnt = int(input())
    print(cnt)

    nums = []

    for i in range(cnt):
        nums.append(input().rstrip().split(" "))
        print(nums[i])
        i += 1

   division(cnt)



if __name__ == '__main__':
    main()