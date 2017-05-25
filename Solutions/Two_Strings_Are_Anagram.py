"""
Q: valid_anagram: Two strings are anagrams
Constraints: O(n) time, O(1) extra space
Example:
Given s = "abcd", t = "dcab", return true.
Given s = "ab", t = "ab", return true.
Given s = "ab", t = "ac", return false.
"""
import collections

def method1(string1, string2):
    # check if two dictionaries are same
    str1 = dict(collections.Counter(string1))
    str2 = dict(collections.Counter(string2))
    return str1 == str2

def method2(string1, string2):
    # check if two sorted strings are same
    return sorted(string1)==sorted(string2)

def method3(string1, string2):
    # list of all alphabets
    # Cons: limited to alphabets
    list1=[0]*26
    list2=[0]*26
    for i in string1:
        list1[ord(i) - ord('a')]+=1
    for i in string2:
        list2[ord(i) - ord('a')]+=1
    return list1==list2


string1 = "aab"
string2 = "aba"
method3(string1,string2)