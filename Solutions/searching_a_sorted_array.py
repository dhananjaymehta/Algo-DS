# Search in Rotated Sorted Array
# For [4, 5, 1, 2, 3] and target=1,
# return 2.


def method1(nums, target):
    l, m, r = 0, 0, len(nums)-1
    while l<=r:  # binary search
        m = l+(r-l)//2
        if nums[m] == target:
            return m
        if nums[l]<=nums[m]:
            if nums[l]<=target<nums[m]:
                r=m-1
            else:
                l=m+1
        else:
            if nums[m]<target<=nums[r]:
                l=m+1
            else:
                r=m-1
    return -1

#N=[0,1,2,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
N=[4,5,6,7,8,9,1,2,3]
T=5
print(method1(nums=N, target=T))