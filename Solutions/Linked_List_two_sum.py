"""
Add Two Numbers in linked list
7->1->6 + 5->9->2. That is, 617 + 295.
"""

class LinkedNode:
    def __init__(self, num):
        self.val=num
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None

    def insert(self,num):
        node=LinkedNode(num)
        node.next=self.head
        self.head=node

    def print_list(self, head, res):
        start=head
        while start:
            res+=str(start.val)+"->"
            start=start.next
            #return res
        return res+"None"


def add_two_numbers(l1, l2):
    head=fake=LinkedNode(-1)
    sum=carry=0

    while l1 or l2 or carry:
        t1 = l1.val if l1 else 0
        t2 = l2.val if l2 else 0
        sum = t1+t2+carry
        carry = sum // 10
        fake.next=LinkedNode(sum % 10)
        fake=fake.next
        if l1:
            l1=l1.next
        if l2:
            l2=l2.next
    return head.next


# linked list 1
LL=linked_list()
LL.insert(3)
LL.insert(1)
LL.insert(9)

# linked list 2
LL1=linked_list()
LL1.insert(8)
LL1.insert(1)
LL1.insert(9)

# add the two lists
ret=add_two_numbers(l1=LL.head, l2=LL1.head)
sol=linked_list()
res=sol.print_list(ret, "")
print(res)