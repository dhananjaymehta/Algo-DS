def longest_valid_palindrome(S):
    val=[]
    l=len(S)
    max_len=""
    for i in range(l):
        if valid_parantheses2(S[i:]):
            max_len= S[i:] if len(max_len)<len(S[i:]) else max_len
    return max_len

def valid_parantheses2(S):
    # space complexity - O(1)
    a = b = 0
    l = len(S)
    for i in range(l):
        if S[i] == '(': a += 1
        if S[i] == ')': b += 1

    return a == b


string="(((())"
print(longest_valid_palindrome(S=string))