# Given an array of integers, find a contiguous subarray which has the largest sum.
# KADANE's Principle
# Ref: http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/


def method1(nums):
    # pure Kadane priciple
    l = len(nums)
    max_so_far = max_current = 0
    for i in range(l):
        # step 1: max ending here
        max_current = max_current + nums[i]
        # step 2: if current < 0 : set to 0
        if max_current < 0: max_current = 0
        # step 3: max so far
        max_so_far = max(max_current, max_so_far)

    return max_so_far


def method2(nums):
    # modified Kadane prnciple
    max_cur= max_so_far=nums[0]
    l = len(nums)
    for i in range(1, l):
        max_cur=max(max_cur+nums[i], nums[i])
        max_so_far=max(max_cur,max_so_far)
    return max_so_far

#N=[-2,2,-3,4,-1,2,1,-5,3]
N=[-2]#, -3, 4, -1, -2, 1, 5, -3]
# [4,−1,2,1] has the largest sum = 6.
print(method1(nums=N))
print(method2(nums=N))

