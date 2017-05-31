# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...


def countAndSay(n):
    res="1"
    if n==0:return None
    if n==1:return res
    for i in range(n-1):
        res=helper(res)
    return res

def helper(num):
    res, count, i = "", 1, 0
    while i<len(num)-1:
        if num[i]==num[i+1]:
            count += 1
        else:
            res += str(count)+num[i]
            count=1
        i+=1
    res+=str(count)+num[i]
    return res

countAndSay(6)
