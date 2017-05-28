# Implement a stack with min() function, which will return the smallest number in the stack.
# It should support push, pop and min operation all in O(1) cost.
"""
| 2 |
-----
| 5 |
-----
| 3 |
-----
| 4 |
-----

transforemed to

| 2,2 |
-------
| 5,3 |
-------
| 3,3 |
-------
| 4,4 |
-------
"""

class MinStack(object):
    def __init__(self):
        self.stack=list()

    def push(self, number):
        # LIFO  - append
        min_ele = self.min()  # find min element
        if min_ele is None or number < min_ele:
            min_ele = number
        self.stack.append((number, min_ele))

    def pop(self):
        # LIFO - pop
        if self.stack == []:
            return None
        else:
            return self.stack.pop()

    def min(self):
        # return min : call pop repeatedly
        if len(self.stack)<1:  # empty stack
            return None
        else:
            return self.stack[-1][1]

St=MinStack()
St.push(3)
St.push(2)
St.push(1)
#print(St.pop())    # return 1
#St.push(2)
#St.push(3)
print(St.min())   #  return 2
print(St.pop())
print(St.min())
print(St.pop())
print(St.min())
# push(3), push(2), push(1), min(), pop(), min(), pop(), min()
# [1,1,2,2,3]

# push(-1), push(-2), min(), pop(), push(-3), push(3), push(2), pop(), pop(), pop(), pop(), push(400), push(3), push(200), push(1), min(), pop(), min()
# [-2,-2,2,3,-3,-1,1,1,3] - expected
# [-2,-2,-3,-3,-3,-1,1,1,3] - actual