# Given an array of n elements which contains elements from 0 to n-1,
# find the repeating elements in array
# http://www.geeksforgeeks.org/?p=9755

def method1(array, size):
    # time complexity --> O(n) and Space --> O(1)
    res=[]
    for i in range(size):
        if array[abs(array[i])]>=0:
            array[abs(array[i])] = -array[abs(array[i])]
        else:
            res.append(abs(array[i]))
    return res

def method2(array, size):
    # time --> O(n) and space --> O(1)
    # first generate all combinations
    for i in range(size):
        ind = array[i]%size
        array[ind] += size
    print(array)
    # arr[i]>1 only if arr i appeared more than once
    for i in range(size):
        if (array[i]//size) > 1:
            print(i)

A=[1,2,3,1,4,3,8,4,8]
#A=[1, 6, 3, 1, 3, 6, 6]
print(method1(array=A, size=len(A)))