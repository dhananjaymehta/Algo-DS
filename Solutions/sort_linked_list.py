"""
Definition of ListNode
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def __init__(self):
        self.head=None

    def insert(self, num):
        node=ListNode(num)
        node.next=self.head
        self.head=node

    def printLL(self, node):
        temp=node
        self.res=[]
        while temp:
            #print(temp.val)
            self.res.append(temp.val)
            temp=temp.next
        print(self.res)
    def sortList(self,head):
        #print("hello")
        self.res.sort()
        #print(self.res)
        self.helper(head)

    def helper(self,head):
        #print(head.val)
        temp=head
        i=0
        while temp:
            temp.val=self.res[i]
            temp=temp.next
            i+=1
        #print(self.head.val)

sol=Solution()
sol.insert(1)
sol.insert(3)
sol.insert(2)
sol.insert(5)
sol.insert(4)
sol.printLL(sol.head)
sol.sortList(sol.head)
sol.printLL(sol.head)


