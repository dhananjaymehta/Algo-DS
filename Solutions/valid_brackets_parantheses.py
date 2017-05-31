# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# input: "()[]{}"
# result: True


def method1(string):
    map_brackets = {'(':')','[':']','{':'}'}  # mapping of
    stack = []    # keep the stack of closing brackets

    for i in range(len(string)):
        if string[i] in map_brackets.keys():        # push closing brackets in stack
            stack.append(map_brackets[string[i]])

        if string[i] in map_brackets.values():      # check closing brackets
            if stack == []:                         # if stack is empty: indicate no more opening brackets
                return False
            if string[i] != stack.pop():            # non-matching brackets
                return False

    return True if stack==[] else False             # if no more closign brackets

S="["
print(method1(string=S))