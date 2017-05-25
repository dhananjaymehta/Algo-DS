from Lintcode import LinkedList


def reverse_linked_list(head):
    prev=None
    curr=head
    while curr:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    head=prev
    return head



LL=LinkedList.LinkedList(5)
# Create first list
LL.insert(6)
LL.insert(4)
LL.insert(9)
LL.insert(5)
LL.insert(7)
LL.printLL(LL.head)
ret=reverse_linked_list(LL.head)
LL.printLL(ret)