def maximumGap(nums):
    # write your code here
    size = max(nums)
    arr = [0]* (size + 1)
    print(arr)
    # traverse the array and set index to 1
    for i in nums:
        arr[i]=1

    # traverse array to find difference:
    max_d=0
    last=arr[min(nums)]
    for i in range(min(nums),len(arr)-1):
        if  arr[i]==1:
            max_d=max(i-last, max_d)
            last=i
    print(max_d)



A=[1, 9, 2, 5]
maximumGap(nums=A)