r"""
Problem: Path Sum
Difficulty: Easy
Category: Trees
LeetCode: #112

Problem Statement:
Given the root of a binary tree and an integer targetSum, return
True if the tree has a ROOT-TO-LEAF path such that the sum of
values along that path equals targetSum.

Example:
Input:      5
           / \
          4   8
         /   / \
        11  13  4
       /  \       \
      7    2       1
targetSum = 22
Output: True  (5 -> 4 -> 11 -> 2 sums to 22)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─────────────────────────────────────────────
# APPROACH: DFS, subtracting as you descend
# Time: O(n) | Space: O(h)
# ─────────────────────────────────────────────

def has_path_sum(root, target_sum):
    """
    Key insight:
    Rather than tracking a running SUM upward, it's cleaner to
    subtract the current node's value from the target as you
    go DOWN — by the time you reach a leaf, checking "does the
    remaining target equal this leaf's value?" is equivalent to
    "did the full path sum to the original target?" This avoids
    needing to pass an accumulated sum back up through return
    values.

    IMPORTANT subtlety: the path must end at a LEAF (no children
    at all) — a common mistake is stopping the check at any None
    child, which would incorrectly accept partial paths that
    happen to sum correctly but don't reach an actual leaf.

    Example walkthrough (target=22):
          5
         / \
        4   8
       /
      11
     /  \
    7    2

    has_path_sum(5, 22): not a leaf, target-val=17
      go left: has_path_sum(4, 17): not a leaf, target-val=13
        go left: has_path_sum(11, 13): not a leaf, target-val=2
          go left: has_path_sum(7, 2): IS a leaf, 7 != 2 → False
          go right: has_path_sum(2, 2): IS a leaf, 2 == 2 → True ✅
    """
    if not root:
        return False   # empty tree has no path at all

    remaining = target_sum - root.val

    if not root.left and not root.right:
        # This IS a leaf — check if the path ending here sums correctly
        return remaining == 0

    # Not a leaf — must continue into at least one existing child
    return (has_path_sum(root.left, remaining) or
            has_path_sum(root.right, remaining))


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    #          5
    #         / \
    #        4   8
    #       /   / \
    #      11  13  4
    #     /  \       \
    #    7    2       1
    root = TreeNode(5,
        TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
        TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))

    assert has_path_sum(root, 22) == True    # 5->4->11->2
    assert has_path_sum(root, 26) == True    # 5->8->13
    assert has_path_sum(root, 100) == False  # no path sums to this

    assert has_path_sum(None, 0) == False    # empty tree, no path exists

    # Single node — the trap case where a naive solution might
    # return True just because 0 - value happens to look right
    # partway through, without actually reaching a real leaf check
    assert has_path_sum(TreeNode(1), 1) == True
    assert has_path_sum(TreeNode(1), 2) == False

    # A node with only ONE child — must not treat it as a leaf
    single_child = TreeNode(1, TreeNode(2))
    assert has_path_sum(single_child, 1) == False   # 1 alone isn't a
                                                       # complete root-to-leaf path

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
DFS with subtraction:
- Time:  O(n) worst case — may need to check every node if no
         valid path exists
- Space: O(h) — recursion stack

KEY PATTERN LEARNED:
The "not root.left and not root.right" leaf check is the exact
detail worth internalizing — checking "remaining == 0" at just
ANY None child (rather than a TRUE leaf) is the most common bug
in this problem, and the single_child test case above is
specifically designed to catch that mistake if it were present.
"""
