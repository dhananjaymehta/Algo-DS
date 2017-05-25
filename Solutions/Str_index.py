"""
For a given source string and a target string,
you should output the first index(from 0) of target string in source string.

return : index if match else -1

 source = "abcdabcdefg"
 target = "bcd"
"""

def returnIndex(string, target):
    # base case check for the nulls
    if string is None or target is None:
        return -1

    t_l=len(target)
    s_l=len(string)
    for i in range((s_l - t_l)+1):
        if string[i:i+t_l]==target:
            return i
    return -1

source = None
target = "abc"
print(returnIndex(source,target))