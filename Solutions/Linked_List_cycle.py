"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """

    def hasCycle(self, head):
        if head is None:  # for case: None
            return False

        slow = head
        if head.next is not None:  # for case: 1->null
            fast = head.next
        else:
            return False

        try:
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next  # jumps two slots
            return True
        except:
            return False
