"""
Compare two strings A and B -
determine whether A contains all of the characters in B.

Example:
    A = "ABCD", B = "ACD", return true.
    A = "ABCD", B = "AABC"
"""
import collections

def contains(A, B):
    ele_A = dict(collections.Counter(A))  # map of elements in A
    ele_B = dict(collections.Counter(B))  # map of elements B

    # if same
    if ele_B==ele_A:
        return True

    # if subset
    if set(ele_B) <= set(ele_A):
        for key in ele_B.keys():
            print(key, ele_A[key],ele_B[key])
            if ele_B[key] <= ele_A[key]:
                continue
            else:
                return False
        return True
    else:
        return False


string1 = "ABSDFABAB"
string2 = "ADB"
print(contains(string1,string2))