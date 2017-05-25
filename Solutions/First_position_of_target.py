def method(arr, target):
    l, r , m = 0, len(arr), 0
    while l < r:
        m=l+(r-l)//2
        if arr[m]==target:
            while m>0 and arr[m]==arr[m-1]:
                m-=1
            return m
        if arr[m]>target:
            r=m
        if arr[m]<target:
            l=m+1
    return -1




A=[1,1,1,1,1,1]#[1, 2, 3, 3, 4, 5, 10] [1,1,1,1,1,1], 1
T=1
print(method(arr=A, target=T))