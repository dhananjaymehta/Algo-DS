# Merge Sorted Array
# A = [1, 2, 3, empty, empty], B = [4, 5]
# size A = len(A) + len(B)

def method(A, m, B, n):
    # traverse both array
    m=m-1
    n=n-1
    print(A[m])
    while m >= 0 and n >= 0:
        if A[m]>B[n]:
            A[m+n+1]=A[m]
            m -= 1
        else:
            A[m+n+1]=B[n]
            n -= 1

    if n >= 0:
        A[:n+1]=B[:n+1]
    return (A)

A = [4,6,7,8, None, None, None, None]
B = [1,2, 4, 5]
method(A,4,B,4)