# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false

def isSymmetric (root):
    def isSym (l,r):
        if not l and not r: return True
        if l and r and l.val == r.val:
            return isSym(l.left, r.right) and isSym(l.right, r.left)
        return False
    return isSym(root,root)