# Given an array with n objects colored red, white or blue,
# sort them so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.
# integers 0, 1, and 2 ==> red, white, and blue respectively


def sort_colors(self, nums):
    l, m, h = 0, 0, len(nums) - 1

    for i in range(len(nums)):
        # -- case1 : if 0
        if nums[m] == 0:
            nums[l], nums[m] = nums[m], nums[l]
            l += 1
            m += 1
        # -- case2 : if 1
        elif nums[m] == 1:
            m += 1
        # -- case3 : if 2
        elif nums[m] == 2:
            nums[m], nums[h] = nums[h], nums[m]
            h -= 1
    print(nums)
