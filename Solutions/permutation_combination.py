def permutation(nums):
    """
    generate permutations of a set of numbers
    :param nums:
    :return:
        set of possible permutations
    """
    l, r = 0, len(nums)-1
    res=[]
    helper_permutation(l, r, nums, res)
    return res


def helper_permutation(l, r, nums, res):
    if l == r:
        temp = nums.copy()
        res.append(temp)

    for i in range(l, r+1):
        nums[i], nums[l] = nums[l], nums[i]
        helper_permutation(l+1,r, nums, res)
        nums[i], nums[l] = nums[l], nums[i]


def combination(nums, k):
    if len(nums) < 2:
        return nums
    l, r = 0, len(nums)-1
    nums.sort()
    res = []  # combinations
    helper_combination(nums, k, l, [], res)
    #combine(len(nums), k, l, [], res)
    print(res)
    return res


def helper_combination(nums, k, l, curr, res):
    if len(curr) == k:
        res.append(curr[:])
        return

    for i in range(l, len(nums)):
        if i > l and nums[i] == nums[i-1]: continue
        curr.append(nums[i])
        helper_combination(nums, k, i+1, curr, res)
        curr.pop()


def combine(n, k, pos, temp,res):
    if len(temp) == k:
        res.append(temp[:])
        return

    for i in range(pos, n):
        temp.append(i+1)
        combine(n, k, i + 1, temp,res)
        temp.pop()

nums = [1, 2, 3, 4]
#print(permutation(nums))
combination(nums,k=2)