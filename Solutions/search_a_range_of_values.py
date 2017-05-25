# Given a sorted array of n integers,
# find the starting and ending position of a given target value.
# [5, 7, 7, 8, 8, 10], Target - 8
# [3, 4]


def method(A, target):
    l, r, m = 0, len(A), 0
    s, e = 0, 0
    while l < r:
        m = l + (r - l) // 2
        print(l,r,m, A[m])
        if A[m] == target:
            s, e = m, m
            while e < r-1 and A[e] == A[e + 1]: # right limit
                e += 1
            print(e)
            while s > l and A[s] == A[s - 1]:  # left limit
                s -= 1
            return [s,e]

        if A[m] > target:
            r = m
        else:
            l = m + 1

    return -1

#nums=[5, 7, 7, 8, 8, 10]
#nums=[1,2,2]
nums=[1]
T=1
print(method(nums, T))
