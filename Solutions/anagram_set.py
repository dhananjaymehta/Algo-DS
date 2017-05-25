import collections
from collections import defaultdict

def method1(anagrams):
    # step 1: generate two list
    l = len(anagrams)
    arr1 = list(range(len(anagrams)))
    arr2 = anagrams[:]

    # step 2: sort alphabets in words in list O(n.mlgm)
    arr2 = [''.join(sorted(arr2[i])) for i in range(l)]

    # step 3: sort the words in list O(nlgn)
    arr3 = list(zip(arr2,arr1))
    arr3.sort(key=lambda x: x[0])

    # step 4: organize result in groups:
    arr4 = {}
    for k,v in arr3:
        arr4[k]=arr4.get(k,[])+[v]

    arr5 = list(arr4.values())

    # step 5:
    res = []
    for grp in arr5:
        if len(grp) > 1:
            [res.append(anagrams[j]) for j in grp]
    print(res)

def method2(anagrams):
    map_ana={}
    for ana in anagrams:
        key=tuple(sorted(ana))
        map_ana[key] = map_ana.get(key, [])+[ana]

    return list(map_ana.values())

anagrams= ["abc", "bca", "de", "f", "ed", "cab"]
#"abc", "bca", "de", "f", "ed", "cab"]
# return ["lint", "inlt", "intl"]
print(method2(anagrams))