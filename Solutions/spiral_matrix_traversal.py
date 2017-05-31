"""
Given a 2D array, print it in spiral form.

Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
"""


def spiral_traversal(M):
    res=[]          # result
    r=len(M)-1      # total rows
    c=len(M[0])-1   # total columns
    k = l = 0       # row: k, col: l

    while k<=r and l<=c:
        # traverse left -> right
        for i in range(l, c+1):
            res.append(M[k][i])
        k += 1    # increase count of rows traversed

        # traverse top -> bottom
        for j in range(k, r+1):
            res.append(M[j][c])
        c -= 1  # decrease column count

        # traverse right -> left
        if r > k:
            for i in range(c, l-1, -1):
                res.append(M[r][i])
            r -= 1    # decrease row count for traversed

        # traverse bottom -> top
        if c > l:
            for j in range(r, k-1, -1):
                res.append(M[j][l])
            l += 1    # increase traversed column

    print(res)

matrix = [[1,  2,  3,  4], [5,  6, 7,  8], [9,  10, 11, 12], [13, 14, 15, 16]]  # 17, 18]]
"""
[1,  2,  3,  4,  5,  6]
[7,  8,  9,  10, 11, 12]
[13, 14, 15, 16, 17, 18]

ans: 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
"""
spiral_traversal(M=matrix)
