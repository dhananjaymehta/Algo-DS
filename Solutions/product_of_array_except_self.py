# Product of Array Exclude Itself
# A = [1, 2, 3],
# return [6, 3, 2]

def method1(array):
    # this is O(n^2)
    res=[]
    for i in range(len(array)):
        x=array[i]
        xs=array[:i]+array[i+1:]
        res.append(helper(xs))
    return res

def helper(array_s):
    #if len(array_s)==2:
    #    return array_s[0]*array_s[1]
    prod = 1
    for i in array_s:
        prod*=i
    return prod

def method2(array):
    # this is O(2n)
    res=[1]*len(array)
    temp=1
    #left pass
    for i in range(len(array)):
        res[i]*=temp
        temp*=array[i]

    temp=1
    #rigth pass:
    for i in range(len(array)-1, -1, -1):
        res[i]*=temp
        temp*=array[i]
    return  res

A = [1, 2, 3, 4]
print(method2(array=A))
