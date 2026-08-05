"""
Problem: Subtree of Another Tree
Difficulty: Easy
Category: Trees
LeetCode: #572

Problem Statement:
Given two binary trees root and subRoot, return True if there
is a subtree of root that is structurally identical (same
structure AND values) to subRoot.

Example:
Input:  root = [3,4,5,1,2], subRoot = [4,1,2]
Output: True  (the subtree rooted at node 4 matches subRoot exactly)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─────────────────────────────────────────────
# APPROACH: Reuse is_same_tree, check at every node
# Time: O(n * m) worst case | Space: O(h)
# ─────────────────────────────────────────────

def is_same_tree(p, q):
    """Directly reused from the Same Tree problem earlier today."""
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def is_subtree(root, sub_root):
    r"""
    Key insight:
    Walk through EVERY node of `root`. At each one, check: "does
    the tree STARTING HERE exactly match sub_root?" using the
    is_same_tree function already built. If any node's subtree
    matches, the answer is True.

    Example walkthrough:
    root:        3            subRoot:   4
                / \                     / \
               4   5                   1   2
              / \
             1   2

    Check at node 3: is_same_tree(root, subRoot)? 3 != 4 → No
    Check at node 4: is_same_tree(node_4_subtree, subRoot)?
                     4==4, 1==1, 2==2 → YES → return True ✅
    (never even needs to check nodes 5, 1, or 2 as starting points)
    """
    if not root:
        return False   # ran out of tree without finding a match

    if is_same_tree(root, sub_root):
        return True

    # Not a match starting here — try starting from each child instead
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    #        3
    #       / \
    #      4   5
    #     / \
    #    1   2
    sub_root = TreeNode(4, TreeNode(1), TreeNode(2))
    root = TreeNode(3, sub_root, TreeNode(5))
    assert is_subtree(root, TreeNode(4, TreeNode(1), TreeNode(2))) == True

    # A node with matching value but WRONG structure underneath —
    # this is the classic trap version of this problem
    #        3
    #       / \
    #      4   5
    #     / \
    #    1   2
    #       /
    #      0
    root2 = TreeNode(3,
        TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))),
        TreeNode(5))
    # subRoot [4,1,2] does NOT match here — node 4's subtree has
    # an extra node (0) that subRoot doesn't have
    assert is_subtree(root2, TreeNode(4, TreeNode(1), TreeNode(2))) == False

    assert is_subtree(root, root) == True   # a tree is always a subtree of itself
    assert is_subtree(None, TreeNode(1)) == False

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Reused comparison at every node:
- Time:  O(n * m) worst case — for each of n nodes in root, an
         is_same_tree check can take up to O(m) where m is the
         size of sub_root
- Space: O(h) — recursion depth of the outer traversal

KEY PATTERN LEARNED:
This directly composes TWO recursive functions together —
is_subtree walks the tree calling is_same_tree at each node,
rather than reimplementing comparison logic from scratch. The
earlier "extra node" test case above is worth remembering
specifically: a naive approach checking only VALUES without full
structural comparison would incorrectly say this matches, since
node 4's value and its direct children's values look right at a
glance — the extra grandchild (0) is what actually breaks it.
"""
