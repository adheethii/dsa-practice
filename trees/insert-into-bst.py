""" 
Problem: Insert into a Binary Search Tree
Difficulty: Medium
Category: Trees / BST
LeetCode: #701

Problem Statement:
Given the root of a BST and a value to insert, insert the value
into the tree such that the BST property is preserved, and return
the root. There may be multiple valid trees — any correct one works.

Example:
Input:  root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]  (5 inserted as the left child of 7)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_sorted_list(self):
        """In-order traversal — for a valid BST this is always sorted."""
        result = []
        if self.left:
            result += self.left.to_sorted_list()
        result.append(self.val)
        if self.right:
            result += self.right.to_sorted_list()
        return result


# ─────────────────────────────────────────────
# APPROACH: Recursive — follow BST ordering to find the insertion spot
# Time: O(h) | Space: O(h)
# ─────────────────────────────────────────────

def insert_into_bst(root, val):
    r"""
    Key insight:
    This directly reuses the same BST-ordering logic from
    yesterday's Lowest Common Ancestor problem — smaller goes
    left, larger goes right — but here the recursion terminates
    by CREATING a new node exactly where the search would
    otherwise have "fallen off" the tree (hit a None).

    Example walkthrough:
    Insert 5 into:
          4
         / \
        2   7
       / \
      1   3

    At 4: 5 > 4 → go right
    At 7: 5 < 7 → go left
    At None (7's left child) → create TreeNode(5) here, attach it

    Result:
          4
         / \
        2   7
       / \  /
      1  3 5
    """
    if not root:
        return TreeNode(val)   # found the insertion spot

    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)

    return root   # always return the (possibly unchanged) root upward


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    #      4
    #     / \
    #    2   7
    #   / \
    #  1   3
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))

    updated = insert_into_bst(root, 5)
    assert updated.to_sorted_list() == [1, 2, 3, 4, 5, 7]   # still sorted -> valid BST

    updated2 = insert_into_bst(updated, 0)
    assert updated2.to_sorted_list() == [0, 1, 2, 3, 4, 5, 7]

    # Inserting into an empty tree
    empty_result = insert_into_bst(None, 10)
    assert empty_result.val == 10
    assert empty_result.left is None and empty_result.right is None

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Recursive BST insertion:
- Time:  O(h) — follows exactly one path from root to leaf
- Space: O(h) — recursion stack

KEY PATTERN LEARNED:
This is the mirror image of BST search/LCA from before: instead
of stopping when a match is found, it stops when it runs OFF the
tree (hits None) and builds a new node there. The line
`root.left = insert_into_bst(root.left, val)` is worth noticing
carefully — it reassigns the child pointer on the way back UP
the recursion, which is what actually attaches the new node into
the existing structure. Forgetting that reassignment is a common
mistake — the recursive call would find the right spot but never
actually link the new node into the tree.
"""
