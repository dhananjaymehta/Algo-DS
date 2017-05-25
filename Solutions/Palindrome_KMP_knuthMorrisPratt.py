"""
Given a string S, you are allowed to convert it to a palindrome by adding characters
in front of it. Find and return the shortest palindrome you can find by performing this transformation.
For example:
Given "aacecaaa", return "aaacecaaa".
Given "abcd", return "dcbabcd".

Knuth–Morris–Pratt string searching algorithm - lead to O(n)

"""

def palindrome(string):
    l = len(string)
    if l % 2 == 0:
        return string[:l // 2] == string[l // 2:][::-1]
    else:
        return string[:l // 2] == string[l // 2 + 1:][::-1]

def question(string):
    l = len(string)-1
    last_pal = 0
    res = ""
    for i in range(l, -1, -1):  # O(n^2)
        if palindrome(string[:i + 1]):
            return string[i + 1:][::-1] + string[0:]
    return res

print(question("abcd"))