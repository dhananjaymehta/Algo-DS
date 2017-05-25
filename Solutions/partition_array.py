# Given an array nums of integers and an int k,
# partition the array (i.e move the elements in "nums") such that:
# All elements < k are moved to the left
# All elements >= k are moved to the right
# --> Return the partitioning index

def method1(nums, k):  # n+nlgn
    # time complexity - O(nlgn)
    nums.sort()  # sort nlgn

    if len(nums)<1 or nums[0]>k:
        return 0
    if nums[-1]<k:
        return len(nums)

    for i in range(len(nums)):
        if nums[i] == k:
            return i

def method2(nums, k):  # nlgn
    # sort around the pivot: k
    # quicksort implementation
    l, r = 0, len(nums)-1
    while l<=r:
        while l <= r and nums[l] < k:
            l += 1
        while l <= r and nums[r] >= k:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
    print(nums)
    print(l)


    #print(l,r)



nums=[9,9,9,8,9,8,7,9,8,8,8,9,8,9,8,8,6,9]
target=9
#print(method1(nums,k=target))
print(method2(nums,k=target))