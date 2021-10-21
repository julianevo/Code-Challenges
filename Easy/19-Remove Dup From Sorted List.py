# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

def deleteDuplicates (head):
    x = head
    while x:
        while x.next and x.next.val == x.val:
            # skip dup node
            x.next = x.next.next 
        # if not a dup move to next node
        x = x.next
    return head