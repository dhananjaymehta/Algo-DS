"""
find the longest common prefix (LCP).
["ABCD", "ABEF", "ACEF"]
LCP is "A"
"""
def method1(strings):
    # this is a brute-force method match each character
    strings.sort()  # O(nlgn)
    #str_m = min(strings, key=len)
    l = len(strings[0])
    i=0
    while i < l:
        for j in range(1,len(strings)):
            if strings[0][i] != strings[j][i]:
                return strings[0][:i]
        i+=1
    return strings[0][:i]

    #def method2(strings):
    # word by word match:
    # http: // www.geeksforgeeks.org / longest - common - prefix - set - 1 - word - by - word - matching /
    # binary search
    # http: //www.geeksforgeeks.org/longest-common-prefix-set-3-divide-and-conquer/


def method2(strings):
    # this is optimized over method1
    if not strings:
        return ""
    l=0
    for ch in zip(*strings):
        if len(set(ch))>1:
            return strings[0][:l]
        l+=1
    return strings[0][:l]


def method3(strings):
    str_m=min(strings, key=len)
    low=0
    high=len(str_m)-1
    mid=0
    res=""
    while low<=high:
        mid=low+(high-low)//2
        if helper(strings, str_m[low:], low, mid):
            res += str_m[low:mid-low+1]
            left = mid+1
        else:
            right = mid-1
    print(res)


def helper(string, ch, l, h):
    # check if all strings contain the character
    for st in strings:
        if st[l:h] != ch:
            return False


strings=["geeksforgeeks", "geeks", "geek", "geezer"]
print(method3(strings))