# Find the contiguous subarray within an array which has the largest product.

def maxProduct(nums):
    # write your code here
    if len(nums) < 1:
        return []
    gmax = nums[0]
    tmax = nums[0]
    tmin = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            tmax, tmin = tmin, tmax
        tmax = max(nums[i], nums[i] * tmax)  # -- max val
        tmin = min(nums[i], nums[i] * tmin)  # -- min val , this becomes max with -ve
        gmax = max(tmax, gmax)  # -- global max

    return gmax

N=[2,3,-2,4,0, -1]
print(maxProduct(nums=N))