# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3


Input: root = [1,null,2]
Output: 2

def maxDepth (root):
    if not root: return 0
    stack = [root]
    depth = 0

    while stack:
        depth += 1
    
        for_ in range(len(stack)):
            tmp = stack.pop(0)
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)

    return depth