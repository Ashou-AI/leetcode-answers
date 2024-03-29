# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Approach 1: Recursion
    time: O(n), space: O(n)
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])  # index of root in the inorder list
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root


class Solution:
    """
    Approach 2: Iteration
    time: O(n), space: O(n)
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return

        root = TreeNode(preorder[0])
        stack = [root]
        idx_inoder = 0

        for i in range(1, len(preorder)):
            child_val = preorder[i]
            node = stack[-1]
            if node.val != inorder[idx_inoder]:
                # construct left subtree at first
                node.left = TreeNode(child_val)
                stack.append(node.left)
            else:
                # construct right subtree
                while stack and stack[-1].val == inorder[idx_inoder]:
                    node = stack.pop()
                    idx_inoder += 1
                node.right = TreeNode(child_val)
                stack.append(node.right)
        return root
