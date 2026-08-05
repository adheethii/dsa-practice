"""
Problem: Diameter of Binary Tree
Difficulty: Easy
Category: Trees
LeetCode: #543

Problem Statement:
Given the root of a binary tree, return the length of the diameter
— the length (in EDGES, not nodes) of the longest path between
any two nodes. This path may or may not pass through the root.

Example:
Input:      1
           / \
          2   3
         / \
        4   5
Output: 3  (path: 4 -> 2 -> 1 -> 3, or equivalently 4 -> 2 -> 5,
            whichever is longer — here 4→2→1→3 has 3 edges)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─────────────────────────────────────────────
# APPROACH: DFS computing depth, tracking diameter as a side effect
# Time: O(n) | Space: O(h)
# ─────────────────────────────────────────────

def diameter_of_binary_tree(root):
    """
    Key insight — the part that trips people up first:
    The longest path does NOT have to pass through the root. It
    could be entirely within the left subtree, or entirely within
    the right subtree. So the diameter must be checked at EVERY
    node, not just computed once at the top.

    The trick: reuse the exact same depth-calculation recursion
    from Maximum Depth of Binary Tree, but at each node, ALSO
    check whether left_depth + right_depth (a path THROUGH this
    node) beats the best diameter seen so far anywhere in the tree.

    Example walkthrough:
          1
         / \
        2   3
       / \
      4   5

    At node 4: left_depth=0, right_depth=0 → path through 4 = 0
    At node 5: left_depth=0, right_depth=0 → path through 5 = 0
    At node 2: left_depth=1 (via 4), right_depth=1 (via 5)
               → path through 2 = 1+1 = 2 → diameter candidate: 2
    At node 3: left_depth=0, right_depth=0 → path through 3 = 0
    At node 1: left_depth=2 (via 2), right_depth=1 (via 3)
               → path through 1 = 2+1 = 3 → diameter candidate: 3

    Best diameter found across ALL nodes = 3 ✅ (matches the
    root-based check here, but that's not guaranteed in general —
    it just happens to be the case in this particular tree)
    """
    diameter = [0]   # use a list as a mutable "nonlocal" holder

    def depth(node):
        if not node:
            return 0

        left_depth = depth(node.left)
        right_depth = depth(node.right)

        # Path through THIS node, in edges: left_depth + right_depth
        diameter[0] = max(diameter[0], left_depth + right_depth)

        # Return depth as normal, for the PARENT's calculation to use
        return 1 + max(left_depth, right_depth)

    depth(root)
    return diameter[0]


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert diameter_of_binary_tree(root) == 3

    # Diameter entirely within a subtree, NOT through the root
    #          1
    #         /
    #        2
    #       / \
    #      3   4
    #     /
    #    5
    root2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(5)), TreeNode(4)))
    # Longest path: 5 -> 3 -> 2 -> 4, which is 3 edges, and does NOT
    # pass through node 1 at all
    assert diameter_of_binary_tree(root2) == 3

    assert diameter_of_binary_tree(TreeNode(1)) == 0   # single node, no edges
    assert diameter_of_binary_tree(None) == 0

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
DFS with side-effect tracking:
- Time:  O(n) — still one pass, depth calculation happens once
         per node, diameter check is O(1) extra work per node
- Space: O(h) — recursion stack

KEY PATTERN LEARNED:
This is the SAME recursive shape as Maximum Depth, with one
addition: at every node, check a value computed FROM that node's
subtree depths against a running global best. The mutable list
trick (diameter = [0]) is a common Python idiom for simulating
a "nonlocal" variable that the inner recursive function can
update — an alternative is using the `nonlocal` keyword directly,
but the list trick is worth recognizing since it appears often
in solutions written by others.
"""
