for _ in range(int(input())):
    nums = sorted(map(int, input().split()))
    for i in range(nums[0], 0, -1):
        if nums[0]%i==0 and nums[1]%i==0:
            print(int(nums[0]*nums[1]/i))
            break