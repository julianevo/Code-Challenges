# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:


def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        def check(nums,start,end):
            if start>end:
                return None
            mid = (start+end)//2
            root = TreeNode(nums[mid])
            root.left = check(nums,start,mid-1)
            root.right = check(nums,mid+1,end)
            return root
        return check(nums,0,n-1)