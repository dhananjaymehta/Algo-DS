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
    s = s[::-1]
    for j, i in enumerate(s):
        # character is not space, a current word exists,
        # and previous character is space, e.g. i=b in " a b":
        if i != " " and word != "" and s[j - 1] == " ":
            # add current word to words and append " " to later add this i
            words += (word + " ")
            word = i
        # character is not space, but it's either first character in string
        # or is part of current word, e.g. i=b in "b", " b" "ab", "a ab "
        elif i != " ":
            word = i + word
        else:
            continue

    words += word

    return (words)
print(reverseWords("how are you?"))
