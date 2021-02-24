'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

example 1: 
1 -> 2 -> 3-> 4 -> 5 turns into 5 -> 4 -> 3 -> 2 -> 1
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        ahead = head
        
        while(ahead!=None):
            ahead = ahead.next
            current.next = prev
            prev = current
            current = ahead
            
        return prev

head = [1,2,3,4,5]
print(reverseList(head))