def valid_parantheses(S):
    # space complexity - O(n)
    val = []
    l = len(S)
    for i in range(l):
        if S[i] == '(':
            val.append(')')
        elif len(val)==0 or val.pop(0)!=')':
            return False

    return True if len(val)==0 else False


def valid_parantheses2(S):
    # space complexity - O(1)
    a=b=0
    l=len(S)
    for i in range(l):
        if S[i]=='(': a += 1
        if S[i]==')': b += 1

    return a==b

string="((()))"
print(valid_parantheses2(S=string))