N = input()
nums = N.split('-')

if len(nums)==1:
    print(sum(map(int, nums[0].split('+'))))

else:
    result = sum(map(int, nums[0].split('+')))
    for n in nums[1:]:
        result -= sum(map(int, n.split('+')))
    print(result)