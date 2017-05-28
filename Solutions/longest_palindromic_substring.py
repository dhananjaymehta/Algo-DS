"""
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

Given the string = "abcdzdcab",
return "cdzdc".
"""


def method1(string):
    # brute force - O(n^2*n)
    # search all possible palindrome
    l=len(string)
    max_pal=""
    for i in range(l-1):
        for j in range(l,i,-1):
            if isPalindrome(string[i:j]):
                if len(max_pal)<len(string[i:j]):
                    max_pal=string[i:j]
    return max_pal

def isPalindrome(S):
    return S==S[::-1]


def method2(string):
    # dynamic programming - O(n^2)
    # Equation: matrix[i][j] = True if matrix[i][j-1] is True and items = self
    l = len(string)
    matrix = [[0]*l for i in range(l)]
    pal = [0, 0]  # pal[0] - length , pal[1] - index

    # last row
    for i in range(1, l):
        if string[i] == string[l-1]:
            matrix[l-1][i] = [1, i]
    # first column
    for j in range(l):
        if string[0] == string[j]:
            matrix[j][0] = [1, j]

    # inner items
    for i in range(l-2,-1,-1):  # row
        for j in range(1,l):    # col
            if matrix[i+1][j-1] != 0 and string[i] == string[j]:
                temp = [matrix[i+1][j-1][0]+1, j]
                matrix[i][j] = temp
                if temp[0] > pal[0]:
                    pal = temp
            elif string[i] == string[j]:
                matrix[i][j] = [1,j]

    return string[pal[1]-pal[0]+1:pal[1]+1]

S="abcdzdcab"
print(method2(string=S))