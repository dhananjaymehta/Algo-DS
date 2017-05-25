"""
Linked List barebone
"""

class linked_list_node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, val):
        self.head=None

    # push a new item into LL - 4 steps
    def insert(self, val):
        # 1 & 2 : Allocate node and put data
        nw_node = linked_list_node(val)
        # 3: point to next or None
        nw_node.next = self.head
        # 4: point head to new node
        self.head=nw_node

    # traverse a linked list
    def printLL(self, head):
        temp=head
        res=""
        while temp:
            #print(temp.data)
            res+=str(temp.data)+"->"
            temp = temp.next
        print(res+"None")
"""
LL=LinkedList(5)
# Create first list
LL.insert(6)
LL.insert(4)
LL.insert(9)
LL.insert(5)
LL.insert(7)
#print(LL.printLL(), "list")
"""