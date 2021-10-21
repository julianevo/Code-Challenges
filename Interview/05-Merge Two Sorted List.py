# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

def mergeTwoLists (a,b):
    if a and b:
        if a.val > b.val:
            a,b = b,a
        a.next = self.mergeTwoLists(a.next, b)
    return a or b

def mergeTwoLists2 (a,b):
    if not a or b and a.val > b.val:
        a, b = b, a
    if a.next = self.mergeTwoLists2(a.next, b)
    return a 