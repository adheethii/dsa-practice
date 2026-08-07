"""
Problem: Balanced Binary Tree
Difficulty: Easy
Category: Trees
LeetCode: #110

Problem Statement:
Given a binary tree, determine if it is height-balanced — for
EVERY node, the depth of its two subtrees never differs by more
than 1.

Example:
Input:      3
           / \
          9  20
             /  \
            15   7
Output: True

Input:         1
              / \
             2   2
            / \
           3   3
          / \
         4   4
Output: False (unbalanced deep on one side)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─────────────────────────────────────────────
# APPROACH (NAIVE — worth understanding why it's inefficient)
# Time: O(n²) worst case
# ─────────────────────────────────────────────

def _height(node):
    if not node:
        return 0
    return 1 + max(_height(node.left), _height(node.right))

def is_balanced_naive(root):
    """
    The obvious first approach: at every node, check whether
    left and right subtree HEIGHTS differ by more than 1, using
    the same height function from Maximum Depth. Looks correct,
    and it IS correct — but it's wasteful.

    The problem: _height() gets called repeatedly on the SAME
    subtrees as the outer recursion descends, recomputing heights
    that were already computed moments earlier by a parent call.
    """
    if not root:
        return True

    left_height = _height(root.left)
    right_height = _height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return is_balanced_naive(root.left) and is_balanced_naive(root.right)


# ─────────────────────────────────────────────
# APPROACH (OPTIMAL — compute height and check balance in ONE pass)
# Time: O(n) | Space: O(h)
# ─────────────────────────────────────────────

def is_balanced(root):
    """
    Key insight:
    Rather than a separate height-check pass ON TOP OF a separate
    balance-check pass (the naive approach's redundancy), do BOTH
    in a single bottom-up traversal. Each recursive call returns
    the subtree's height — but returns -1 as a special "already
    found unbalanced somewhere below" signal that immediately
    propagates up and short-circuits everything above it.

    Example walkthrough:
          3
         / \
        9  20
           /  \
          15   7

    check(9): no children → height 1, balanced
    check(15): no children → height 1, balanced
    check(7): no children → height 1, balanced
    check(20): left height=1, right height=1, diff=0 ≤1 →
               balanced, returns height 1+max(1,1)=2
    check(3): left height=1 (from 9), right height=2 (from 20)
              diff=1 ≤1 → balanced, returns height 1+max(1,2)=3

    No -1 ever appeared → tree is balanced ✅
    """
    def check(node):
        if not node:
            return 0   # height of an empty subtree

        left_height = check(node.left)
        if left_height == -1:
            return -1   # unbalanced already found below — propagate up immediately

        right_height = check(node.right)
        if right_height == -1:
            return -1   # same, from the right side

        if abs(left_height - right_height) > 1:
            return -1   # THIS node is unbalanced

        return 1 + max(left_height, right_height)

    return check(root) != -1


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    #        3
    #       / \
    #      9  20
    #         /  \
    #        15   7
    balanced_tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert is_balanced(balanced_tree) == True
    assert is_balanced_naive(balanced_tree) == True

    #           1
    #          / \
    #         2   2
    #        / \
    #       3   3
    #      / \
    #     4   4
    unbalanced_tree = TreeNode(
        1,
        TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
        TreeNode(2),
    )
    assert is_balanced(unbalanced_tree) == False
    assert is_balanced_naive(unbalanced_tree) == False

    assert is_balanced(None) == True   # an empty tree is trivially balanced
    assert is_balanced(TreeNode(1)) == True   # single node is trivially balanced

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Naive approach:
- Time:  O(n²) worst case — _height() is called on overlapping
         subtrees repeatedly as the outer recursion descends,
         particularly bad on a skewed (linked-list-shaped) tree

Optimal (single-pass with -1 sentinel):
- Time:  O(n) — each node's height is computed exactly once
- Space: O(h) — recursion stack

KEY PATTERN LEARNED:
The -1-as-sentinel-value trick is genuinely worth internalizing:
it's a common way to make a bottom-up tree recursion do TWO jobs
at once (compute a real value AND signal an early-exit condition)
without needing two separate return values or an external mutable
flag. This early-short-circuit approach — the moment ANY subtree
is found unbalanced, stop doing further work above it — is the
same underlying idea as short-circuit evaluation in boolean logic,
just applied to a tree recursion instead.
"""
