"""
Problem: Validate Binary Search Tree
Difficulty: Medium
Category: Trees
LeetCode: #98

Problem Statement:
Given the root of a binary tree, determine if it is a valid BST.
A valid BST: left subtree values < node value < right subtree values,
for EVERY node (not just immediate children).

Example:
Input:  [5,1,4,null,null,3,6]
Output: False (4 is in right subtree of 5, but 4 < 5 violates rule... 
         wait: node 4's left child is 3, but 3 must be > 4's own 
         ancestor constraints — 4 itself is < 5 but placed in right 
         subtree of 5, which requires > 5. Invalid.)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─────────────────────────────────────────────
# APPROACH: DFS with Min/Max Bounds (Optimal)
# Time: O(n) | Space: O(h) — h = tree height
# ─────────────────────────────────────────────

def is_valid_bst(root):
    """
    Key insight:
    A common MISTAKE is only checking node.left.val < node.val
    < node.right.val — this misses violations from GRANDCHILDREN.

    Correct approach: pass down a valid RANGE (min, max) for each
    node. Going left tightens the max bound; going right tightens
    the min bound.

    Example walkthrough:
    Tree: 5 with right child 4 (invalid: 4 must be > 5's range... 
    but let's trace a valid case)

    Tree:      5
              / \\
             3   8

    validate(5, min=-inf, max=+inf): 5 is in range ✓
      validate(3, min=-inf, max=5):  3 is in range ✓ (must be < 5)
      validate(8, min=5, max=+inf):  8 is in range ✓ (must be > 5)

    All valid → True
    """
    def validate(node, low, high):
        if not node:
            return True   # empty tree/subtree is valid

        if not (low < node.val < high):
            return False   # violates the range constraint

        # Left subtree: all values must be < node.val (tighten max)
        # Right subtree: all values must be > node.val (tighten min)
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))

    return validate(root, float('-inf'), float('inf'))


# ─────────────────────────────────────────────
# APPROACH 2: In-order Traversal (should be sorted)
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────

def is_valid_bst_inorder(root):
    """
    A BST's in-order traversal MUST produce a strictly
    increasing sequence — check this property instead.
    """
    values = []

    def inorder(node):
        if node:
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

    inorder(root)

    for i in range(1, len(values)):
        if values[i] <= values[i-1]:
            return False

    return True


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # Valid BST:      5
    #                / \
    #               3   8
    valid = TreeNode(5, TreeNode(3), TreeNode(8))
    assert is_valid_bst(valid) == True

    # Invalid BST:    5
    #                / \
    #               1   4
    #                  / \
    #                 3   6
    invalid = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid_bst(invalid) == False

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Min/Max Bounds DFS:
- Time:  O(n) — visit every node once
- Space: O(h) — recursion stack, h=height (O(log n) balanced, O(n) skewed)

KEY PATTERN LEARNED:
The classic mistake in BST validation is only checking immediate
children. The correct pattern PASSES DOWN a valid (min, max) range
that tightens as you go deeper — this correctly catches violations
from any ancestor, not just the direct parent.
"""
