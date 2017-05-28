"""
Given s = "the sky is blue",
return "blue is sky the".
"""
def reverseWords(string):
    # reverse entire string
    string = string[::-1]
    last = 0
    s=[i for i in string]

    # reverse every word
    for i in range(len(s)):
        if s[i] == " ":
            s[last:i] = s[last:i][::-1]
            last = i + 1
        if i == len(s) - 1:
            s[last:i+1] = s[last:i+1][::-1]
            #last = i + 1
    return "".join(s)


def reverseWords2(s):
    word = ""
    words = ""
    s=s[::-1]

    for j, i in enumerate(s):
        if i != " " and word != "" and s[j-1] == " ":
            words += (word+" ")
            word = i
        elif i != " ":
            word = i + word
        else:
            continue

    words += word
    return words




print(reverseWords2("how are you my friend?"))
