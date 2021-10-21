# Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [1,3,2]


Input: root = [1,null,2]
Output: [1,2]

Recursively

def orderTraversal (root):
    res = []
    self.helper(root,res)
    return res

def helper (root res):
    if root:
        self.helper(root.left,res)
        res.append(root.val)
        self.helper(root.right,res)


Stack method

def orderTraversal2 (root):
    stack = []
    result = []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.val)
        root = root.right
    return result