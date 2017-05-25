# generate permutations of numbers in an array

def permutation(N):
    res = []
    helper(N, res, 0, len(N)-1)
    return res


def helper(nums, res, l, r):
    if l == r:
        res.append(nums[:])

    for i in range(l,r+1):
        nums[i], nums[l] = nums[l], nums[i]
        helper(nums, res, l+1, r)
        nums[i], nums[l] = nums[l], nums[i]


def permutation2(nums):
    res = []
    dfs(nums, [], res)
    return res


def dfs(nums, path, res):
    if not nums:
        res.append(path)
        return      # backtracking
    for i in range(len(nums)):
        x=nums[i]
        x_s=nums[:i] + nums[i + 1:]
        #print(x_s)
        dfs(x_s, path+[x], res)


nums=[1,2,3]
print(permutation(N=nums))
print(permutation2(nums))