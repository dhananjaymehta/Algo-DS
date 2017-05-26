def valid_parantheses(S):
    # complexity 
    val = []
    l = len(S)
    for i in range(l):
        if S[i] == '(':
            val.append(')')
        elif len(val)==0 or val.pop(0)!=')':
            return False

    return True if len(val)==0 else False


string="((()))"
print(valid_parantheses(S=string))