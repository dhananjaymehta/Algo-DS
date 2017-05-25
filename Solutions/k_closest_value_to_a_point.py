def k_nearest(K, X, nums):
    # find the intersection
    inter=intersect(X, nums)
    for

def intersect(X, nums):
    l, r, m = 0, len(nums), 0
    while l<r:
        m=l+(r-l)//2
        if nums[m]==X:
            return m
        if nums[m]<X:
            l=m+1
        if nums[m]>X:
            r=m
    return l




K = 4
X = 35
nums=[12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
k_nearest(K, X, nums)