# Author: Dhananjay Mehta
# Problem: Generate power set for a set of character
# time complexity : O(n.2^n)
import math


def powerset(nums):
    """
    this function generate powerset for a set of characters
    :param nums: set of characters
    :return:
     power set of nums
    """
    l = len(nums)
    pow_size = int(math.pow(2,l))  # size of powerset
    res = []  # initializing the powerset

    # generate the powerset:
    for i in range(pow_size):
        bin_val = '{:032b}'.format(i)[-l:]  # convert to binary equivalent
        tmp = ''
        for j, k in enumerate(bin_val):
            if k == str(1):
                tmp += str(nums[j])
        res.append(tmp)
    return res

nums = ['1','2','3']
result = powerset(nums)
print(result)

