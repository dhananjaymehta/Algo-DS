def method1(nums, k):
    import bisect
    return bisect.bisect(nums,k)

def method2(nums,k):
    l, r , m = 0, len(nums), 0
    while l<r:
        m=l+(r-l)//2
        if nums[m] == k:
            return m
        if nums[m] < k:
            l=m+1
        if nums[m] > k:
            r=m
    return l

def method3(nums,k):
    l, r , m = 0, len(nums)-1, 0
    while l<=r:
        m=l+(r-l)//2
        if nums[m] == k:
            return m
        if nums[m] < k:
            l=m+1
        if nums[m] > k:
            r=m-1
    return l


#N=[1,10,1001,201,1001,10001,10007]
#K=10008
#N=[1,2,3,4,5,9]
#K=0
N=[1,3,5,6,8,9]
K=10
print(method3(nums=N, k=K))