# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.


def twoSum(nums, target):
    map_2sum = {}
    for i in range(len(nums)):
        # print(nums, nums[i], map_2sum)
        if nums[i] in map_2sum:
            # print(nums, nums[i], map_2sum)
            return (map_2sum[nums[i]]+1, i + 1)
        else:
            if target - nums[i] not in map_2sum:
                map_2sum[target - nums[i]] = map_2sum.get(target - nums[i], 0) + i
    return []

# T1: a= [2, 7, 11, 15]
a=[1,1,1,1,1,8]
t= 9
print(twoSum(nums=a, target=t))

