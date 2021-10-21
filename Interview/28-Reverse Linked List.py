# Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

def reverseList (head):
    prev = None
    cur = head

    while cur:
        # locate next node
        x = cur.next
        # reverse direction
        cur.next = prev
        prev = cur
        cur = x
    # new head of reverse linked list    
    return prev