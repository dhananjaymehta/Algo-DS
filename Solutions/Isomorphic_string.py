import collections

def isIsomorphic(s,t):
    mp_s = dict(collections.Counter(s))
    mp_t = dict(collections.Counter(t))
    return sorted(mp_s.values()) == sorted(mp_t.values())


def isIsomorphic2(s,t):
    d1, d2 = {}, {}
    for i, val in enumerate(s):
        d1[val] = d1.get(val, []) + [i]
    for i, val in enumerate(t):
        d2[val] = d2.get(val, []) + [i]
    return sorted(d1.values()) == sorted(d2.values())

s="foo"
t="bar"
print(isIsomorphic(s,t))