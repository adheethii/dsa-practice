r"""
Problem: Invert Binary Tree
Difficulty: Easy
Category: Trees
LeetCode: #226

Problem Statement:
Given the root of a binary tree, invert it — swap every node's
left and right children — and return the new root.

Example:
Input:      4                Output:      4
           / \                           / \
          2   7                         7   2
         / \  / \                      / \  / \
        1  3 6   9                    9  6  3  1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─────────────────────────────────────────────
# APPROACH: Recursive swap
# Time: O(n) | Space: O(h)
# ─────────────────────────────────────────────

def invert_tree(root):
    r"""
    Key insight:
    At every node, swap its left and right pointers, then
    recurse into both children (which, after the swap, are
    already in their final positions relative to the parent).

    Example walkthrough (single level):
        4                4
       / \      →       / \
      2   7             7   2
    """
    if not root:
        return None

    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    #        4
    #       / \
    #      2   7
    #     / \  / \
    #    1  3 6   9
    root = TreeNode(4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(7, TreeNode(6), TreeNode(9)))

    inverted = invert_tree(root)

    assert inverted.val == 4
    assert inverted.left.val == 7
    assert inverted.right.val == 2
    assert inverted.left.left.val == 9
    assert inverted.left.right.val == 6
    assert inverted.right.left.val == 3
    assert inverted.right.right.val == 1

    assert invert_tree(None) is None
    assert invert_tree(TreeNode(1)).val == 1

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Recursive swap:
- Time:  O(n) — visits every node once
- Space: O(h) — recursion stack

KEY PATTERN LEARNED:
The simplest possible tree MUTATION pattern — swap at each node,
recurse into both sides. Famously the problem that became a
meme (the creator of Homebrew was once asked this in a Google
interview and failed it), which is a good reminder that even
simple-looking tree recursion can trip people up under
interview pressure if the recurse-then-combine template isn't
second nature yet.
"""
