# http://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/

# Find the longest substring with k unique characters in a given string

# Test cases:
# "aabbcc", k = 1 -> aa, bb, cc
# "aabbcc", k = 3 -> aabbcc
# "aaabbb", k = 3 -> -1, 2 characters
# "aabcdcdcdcdbd" , k=3
import collections


def method1(string, k):
    """
    bruteforce approach to find : O(n^2)*O(n) -> O(n^3)
    :param string:
    :param k:
    :return:
    """
    l=len(string)
    g_string=""#global string
    for i in range(l):
        for j in range(i+1):
            elements = dict(collections.Counter(string[j:i+1])).keys()
            if len(elements)==k:
                if len(string[j:i+1])>len(g_string):
                    g_string=string[j:i+1]

    print(g_string)


def method2(string, k):
    """
    This takes linear time.
    :param string: string
    :param k: target
    :return:
    """
    l=len(string)
    queue=[]
    g_str=list()
    for i in range(l):
        queue.append(string[i])
        elements=dict(collections.Counter(queue)).keys()
        if len(elements) == k and len(g_str)<len(queue):
            g_str = queue
        if len(elements) > k:
            del queue[0]
    print(''.join(i for i in g_str))


nums = "aabbcc"
target = 1
#method1(nums,target)
#method2(nums,target)


