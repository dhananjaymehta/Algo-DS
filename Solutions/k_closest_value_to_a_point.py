# Given a sorted array arr[] and a value X,
# find the k closest elements to X in arr[]
# Input: K = 4, X = 35
# arr[] = {12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56}
# Output: 30 39 42 45


def k_nearest(K, X, nums):
    Leng=len(nums)

    # find the intersection
    m=intersect(X, nums)

    l=m-1 if nums[m]==X else m
    r=m+1
    count=0
    res=[]

    # find K closes points
    while l >= 0 and r<Leng and count<K:
        if nums[m]-nums[l]<nums[r]-nums[m]:
            res.append(nums[l])
            l -= 1
        else:
            res.append(nums[r])
            r += 1
        count+=1

    # if reached right limit
    if count<K and l>=0:
        res.append(nums[l])
        l-=1
        count+=1

    # if reached left limit
    if count < K and r<l:
        res.append(nums[l])
        l -= 1
        count += 1

    print(res)


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