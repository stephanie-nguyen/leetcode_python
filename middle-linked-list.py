'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
'''

import pdb
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    slow=head
    fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
    #pdb.set_trace()
    return slow.val

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(middleNode(head)) 