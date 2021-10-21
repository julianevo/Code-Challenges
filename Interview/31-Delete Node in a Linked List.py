# Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

# It is guaranteed that the node to be deleted is not a tail node in the list.

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

def deleteNode (node):
    # locate node
    victim = node.next

    # overwrite node's value w/ victim
    node.val = victim.val

    # break the linkage of victim
    node.next = victim.next

    # release the victim 
    del victim

    return 