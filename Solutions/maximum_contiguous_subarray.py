def max_subarray(nums):
    # using Kadane principle - O(n)
    # step 1: max_cur, max_glob
    max_cur=0
    max_glob=-float('inf')
    for i in nums:
        max_cur+=i
    # step 2: check global
        max_glob=max(max_cur, max_glob)

    # step 3: reset max_cur
        max_cur=0 if max_cur<0 else max_cur
        print(max_cur, max_glob, i)

#nums =[-2, 1, -3, 4, -1, 2, 1, -5, 4]
#nums = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
nums = [-2, -3, 4, -1, -2, 1, 5, -3]
max_subarray(nums)