# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Generic setup for relative velocity pointers
def relative_velocity_pointers(head: ListNode):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # PROCESS VALUES AT POINTERS
    return

# Reverse a linked list
def reverse_linked_list(head: ListNode) -> ListNode:
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev