"""
Problem: Same Tree
Difficulty: Easy
Category: Trees
LeetCode: #100

Problem Statement:
Given the roots of two binary trees, check if they are the same
— structurally identical AND with the same node values.

Example:
p = [1,2,3], q = [1,2,3] → True
p = [1,2],   q = [1,None,2] → False (different structure)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    """
    Base case FIRST, always, for tree recursion: if both are None,
    they match (both empty). If only ONE is None, they can't
    match. Otherwise compare values and recurse on both children.
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == "__main__":
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_same_tree(p1, q1) == True

    p2 = TreeNode(1, TreeNode(2))
    q2 = TreeNode(1, None, TreeNode(2))
    assert is_same_tree(p2, q2) == False   # same values, different structure

    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))
    assert is_same_tree(p3, q3) == False   # same values, wrong positions

    assert is_same_tree(None, None) == True
    assert is_same_tree(TreeNode(1), None) == False

    print("✅ All test cases passed!")

"""
KEY PATTERN LEARNED:
This is the base template every other "compare two trees" problem
builds on — Symmetric Tree (below) and Subtree of Another Tree
both reduce to calling something like this repeatedly. Get the
None-handling right here first: both None -> match, exactly one
None -> mismatch, is the two-line check that's easy to get
subtly wrong under pressure.
"""
