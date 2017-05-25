"""
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
"""


def method(arr, target):
    row=len(A)
    col=len(A[0])-1
    r=0 # -- start from top right

    while r<row and col>=0:
        if arr[r][col] == target:  # if a match
            return r, col
        if arr[r][col] > target:  # if greater than
            col -= 1
        else:# arr[r][col] < target:  # if lower than
            r += 1

    return 0


A=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
T=21
print(method(arr=A, target=T))