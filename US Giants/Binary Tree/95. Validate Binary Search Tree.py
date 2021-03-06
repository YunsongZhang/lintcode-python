class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        root_valid, _, _ = self.divide_conquer(root)

        return root_valid

    def divide_conquer(self, root):
        if root is None:
            return True, None, None

        left_valid, left_min, left_max = self.divide_conquer(root.left)
        right_valid, right_min, right_max = self.divide_conquer(root.right)

        if not left_valid or not right_valid:
            return False, None, None
        if left_max is not None and left_max.val >= root.val:
            return False, None, None
        if right_min is not None and right_min.val <= root.val:
            return False, None, None

        min_node = left_min if left_min is not None else root
        max_node = right_max if right_max is not None else root

        return True, min_node, max_node
