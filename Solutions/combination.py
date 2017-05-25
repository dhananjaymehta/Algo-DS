# Given two integers n and k,
# return all possible combinations of k numbers out of 1 ... n.
# For example,
# If n = 4 and k = 2, a solution is:
# [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]


def combination(nums, k):
    if len(nums)<1:
        return nums
    res=[]
    helper(nums, res, 0, k, [])
    return res


def helper(nums, res, l, k, temp):
    if len(temp)==k:
        res.append(temp[:])
        return

    for i in range(l, len(nums)):
        if nums[i] == nums[i-1] and i > l: continue
        temp.append(nums[i])
        helper(nums, res, i+1, k, temp)
        temp.pop()

nums=[1,2,3,4]
k=2
print(combination(nums, k))