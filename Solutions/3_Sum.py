# Given an array S of n integers, are there elements a, b, c in S
# such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
def three_sum(arr):
    # write your code here
    size = len(arr)
    arr.sort()  # -- sort the numbers
    res = []  # --result

    for i in range(size - 2):
        if arr[i] == arr[i - 1] and i > 0: continue
        l, r = i+1, size - 1
        while l < r:
            s = arr[i] + arr[l] + arr[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([arr[i], arr[l], arr[r]])
                while l < r and arr[l] == arr[l + 1]:
                    l += 1
                while l < r and arr[r] == arr[r - 1]:
                    r -= 1
                l += 1; r -= 1
    return res

def three_sum_closest(nums, target):
    size = len(nums)
    if size<3:
        return None

    nums.sort()  # sort the items
    res=list()  # result
    tot_d = float('inf')  # difference from target
    for i in range(size-2):  # fix one item
        l, r = i+1, size-1
        while l<r:  # move inner items
            s = nums[i]+nums[l]+nums[r]
            diff=abs(target - (s))
            # difference from current sum
            if diff < tot_d:
                tot_d = diff
                res = [nums[i], nums[l], nums[r]]
            if s > target:
                r -= 1
            else:
                l += 1
    return res

#A=[2,0,-2,-1,-1,2,-4,6]
A=[-1, 2, 1, -4]
K=1
#print(three_sum(A))
print(three_sum_closest(nums=A, target=K))
