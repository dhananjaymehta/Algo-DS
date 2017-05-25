# Given an unsorted integer array, find the first missing positive integer.
# [1,2,0] return 3,
# [3,4,-1,1] return 2.
# http://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/

import collections
import math

def method1(array):
    # this will be O(nlgn)
    array.sort()  # sorting nlgn
    max = 0
    for i in range(len(array)):
        if array[i] >- 1 and array[i] == max+1:
            max = array[i]
    return max+1


def method2(array):
    # this will be O(n) time and O(n) space
    items= list(dict(collections.Counter(array).keys()))  #O(2*n)
    max=0
    for i in range(len(items)):
        if items[i]==max+1:
            max = items[i]
    return max+1


def method3(array):
    # this will use O(n) time and O(1) space
    def separate(array):  # separate positves and negatives in an array O(n)
        j=0
        for i in range(len(array)):
            if array[i]<=0:
                array[j],array[i]=array[i],array[j]
                j+=1
        return array, j

    def find_missing_positive(array, size):
        # find the missing value

        for i in range(size):
            if abs(array[i])-1 < size and array[abs(array[i])-1] > 0:
                array[abs(array[i]) - 1] = -array[abs(array[i]) - 1]

        for i in range(size):
            if array[i]>0:
                return i+1
        return size+1

    array, shift = separate(array)
    return find_missing_positive(array[shift:], len(array[shift:]))

A=[99,94,96,11,92,5,0,9]
#print(method1(array=A))
#print(method2(array=A))
print(method3(array=A))