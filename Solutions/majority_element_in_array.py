import collections
"""
Given an array of integers, the majority number is the number that occurs more
than half of the size of the array. Find it

input: [1, 1, 1, 1, 2, 2, 2],
return: 1
"""


def method1(nums):
    # write your code here
    th = len(nums) // 2
    map_count = dict(collections.Counter(nums))

    for k, val in map_count.items():
        if len(nums) % 2 == 0:
            if val >= th:
                return k
        else:
            if val > th:
                return k
    return -1


def method2(nums):
    # create map O(n)
    s = collections.Counter(nums)
    # traverse map O(n)
    return [i for i in nums if s[i] > len(nums) // 2][0]


def method3(nums):
    # create map O(n)
    s = collections.Counter(nums)
    # traverse
    for i in s:
        if s[i]>len(nums)//2: return i


N = [1, 1, 1, 1, 2, 2, 2]
print(method1(nums=N))
print(method2(nums=N))
print(method3(nums=N))