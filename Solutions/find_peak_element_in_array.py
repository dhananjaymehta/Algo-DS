"""
Find a peak element in this array. Return the index of the peak.

The numbers in adjacent positions are different.
    A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
"""

def method(nums, size):
    l, r, m = 1, size-1, 0
    while l<r:
        m=l+(r-l)//2
        if nums[m]>nums[m-1] and nums[m]>nums[m+1]:
            return m,nums[m]
        if nums[m]<nums[m+1]:
            l=m+1
        else:
            r=m
        print(l, r, m, nums[m])


def method2(nums, size):
    # this method works even when the array is not ordered as above
    # this is faster
    l, r, m = 0, size - 1, 0
    while l < r:
        m = l + (r - l) // 2
        print(l, r, m, nums[l])
        if nums[m] > nums[m + 1]:
            r = m
        if nums[m] < nums[m + 1]:
            l = m + 1
    return l


N=[1,2,3,4,5,6]
print(method(nums=N, size=len(N)))
print("second")
print(method2(nums=N, size=len(N)))