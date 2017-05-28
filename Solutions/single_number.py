"""
Given 2*n + 1 numbers, every numbers occurs twice except one, find it.
Given [1,2,2,1,3,4,3], return 4
"""
import collections
from functools import reduce


def singleNumber(A):
    # O(n) time and O(n) space - 216ms
    if len(A) < 1:
        return 0
    d = dict(collections.Counter(A))
    for i in d:
        if d[i] == 1:
            return i

def singleNumber2(A):
    # O(n+nlgn) time and O(1) space - 226ms
    if len(A) < 1:
        return 0
    A.sort()
    print(A)
    for i in range(0, len(A) - 1, 2):
        print(i,A[i],A[i+1])
        if A[i] != A[i + 1]:
            return A[i]
    return A[-1]

def singleNumber3(A):
    # O(n) time and O(1) space - 230ms
    unique=set()
    dups=set()
    for i in A:
        if i not in unique:
            unique.add(i)
        else:
            dups.add(i)
    #print(unique, dups)
    return list(unique-dups)[0]


def singleNumber4(A):
    # O(n/2) time and O(1) space - 210 ms
    if len(A)<1:
        return 0

    return reduce(lambda x, y: x ^ y, A)


A=[1,4,2,1,2,3,3]
#print(singleNumber(A))
print(singleNumber4(A))