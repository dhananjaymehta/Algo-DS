# Given a string, find the length of the longest substring without repeating characters.
# "abcabcbb" is "abc", which the length is 3.
# "bbbbbb" is "b", length 1

def method1(string):
    visited={}
    start=0
    max_l=i=0
    l=len(string)
    while i<l:
        if string[i] in visited and start<=visited[string[i]]:
            start=visited[string[i]]+1
        else:
            max_l=max(max_l, i-start+1)
        visited[string[i]]=i
        i+=1
    print(max_l, string[start:])

method1("an++--viaj")#ccddeefefgh")