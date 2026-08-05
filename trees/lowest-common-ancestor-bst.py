"""
Problem: Lowest Common Ancestor of a Binary Search Tree
Difficulty: Medium
Category: Trees
LeetCode: #235

Problem Statement:
Given a BST and two node values p and q, find their lowest
common ancestor (LCA) — the deepest node that has both p and q
as descendants (a node can be a descendant of itself).

Example:
Input: root of BST, p=2, q=8
Output: node with value 6
(2 and 8 are both descendants of 6, and 6 is the deepest such node)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─────────────────────────────────────────────
# APPROACH: Use the BST property directly (no full traversal needed)
# Time: O(h) | Space: O(h) recursive, O(1) iterative
# ─────────────────────────────────────────────

def lowest_common_ancestor(root, p_val, q_val):
    """
    Key insight — this is specifically about a BST, not just any
    binary tree, and that structure makes this MUCH simpler than
    the general binary tree LCA problem:

    Because of the BST ordering property (left < node < right),
    at any given node we can tell WHICH DIRECTION to go without
    exploring both subtrees:

    - If BOTH p and q are smaller than the current node's value,
      the LCA must be somewhere in the LEFT subtree
    - If BOTH p and q are larger, the LCA must be in the RIGHT subtree
    - Otherwise (one is smaller, one is larger, or one equals the
      current node), the current node IS the split point — this
      is the LCA

    Example walkthrough (values only, structure is a BST):
              6
            /   \
           2     8
          / \   / \
         0   4 7   9

    Find LCA of 2 and 8:
    At node 6: is 2 < 6? yes. Is 8 < 6? no.
               → they split here → 6 IS the LCA ✅ (no need to recurse further)

    Find LCA of 0 and 4:
    At node 6: both 0 and 4 are < 6 → go left
    At node 2: is 0 < 2? yes. Is 4 < 2? no.
               → split here → 2 IS the LCA ✅
    """
    node = root

    while node:
        if p_val < node.val and q_val < node.val:
            node = node.left     # both targets are smaller — go left
        elif p_val > node.val and q_val > node.val:
            node = node.right    # both targets are larger — go right
        else:
            return node          # split point found — this is the LCA


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    #              6
    #            /   \
    #           2     8
    #          / \   / \
    #         0   4 7   9
    #            / \
    #           3   5
    n0 = TreeNode(0)
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n4 = TreeNode(4, n3, n5)
    n2 = TreeNode(2, n0, n4)
    n7 = TreeNode(7)
    n9 = TreeNode(9)
    n8 = TreeNode(8, n7, n9)
    root = TreeNode(6, n2, n8)

    # LCA of 2 and 8 should be 6 (root is the split point)
    result = lowest_common_ancestor(root, 2, 8)
    assert result.val == 6

    # LCA of 0 and 4 should be 2
    result = lowest_common_ancestor(root, 0, 4)
    assert result.val == 2

    # LCA of a node and itself should be that node
    result = lowest_common_ancestor(root, 4, 4)
    assert result.val == 4

    # LCA of 3 and 5 should be 4 (their direct parent)
    result = lowest_common_ancestor(root, 3, 5)
    assert result.val == 4

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
BST-property-based search:
- Time:  O(h) — h = tree height, since each step moves down one
         level toward the answer, never both subtrees
- Space: O(h) for a recursive version, O(1) for this iterative one

KEY PATTERN LEARNED:
This is notably CHEAPER than LCA on a general binary tree (which
needs O(n) and must explore both subtrees, since there's no
ordering to exploit). The lesson worth generalizing: always check
whether a problem's SPECIFIC structure (sorted, BST-ordered,
etc.) can be exploited to avoid a full traversal, rather than
reaching immediately for the general-case algorithm out of habit.
"""
