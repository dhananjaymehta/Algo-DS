def method(arr, size):
    l, r, m = 0, size-1, 0

    while l<r:
        m = l+(r-l)//2
#        print(l,r,m, arr[m])
        if arr[m]>arr[r]:
            l=m+1
        else:
            r=m
    return arr[l]

A=[4, 5, 6, 7, 8, 9, 1, 2]
print(method(arr=A, size=len(A)))