def square_root(num):
    l=0; r=num
    while l < r:
        mid = l + (r-l)//2
        if mid**2<=num<(mid+1)**2:
            return mid
        if mid**2>num:
            r = mid
        if mid**2<num:
            l = mid+1
    return l

N=0
print(square_root(num=N))