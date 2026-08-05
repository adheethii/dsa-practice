r"""
Problem: Binary Tree Right Side View
Difficulty: Medium
Category: Trees / BFS
LeetCode: #199

Problem Statement:
Given the root of a binary tree, imagine standing on the RIGHT
side of it — return the values of the nodes you can see, ordered
from top to bottom.

Example:
Input:      1
           / \
          2   3
           \    \
            5    4
Output: [1,3,4]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─────────────────────────────────────────────
# APPROACH: BFS — take the LAST node of each level
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────

def right_side_view(root):
    r"""
    Key insight:
    Directly reuses the level-order BFS structure from the
    previous problem today, with one change: instead of
    collecting every value in the level, only keep the LAST
    node processed in each level's inner loop — that's exactly
    the rightmost node visible from that level.

    Example walkthrough:
          1
         / \
        2   3
         \    \
          5    4

    Level 0: queue processes [1] → last node = 1 → result=[1]
    Level 1: queue processes [2,3] → last node = 3 → result=[1,3]
             (2 is pushed before 3, so 3 is processed last — this
              works because children are always pushed left-then-
              right, keeping right-side nodes naturally last)
    Level 2: queue processes [5,4] → last node = 4 → result=[1,3,4]
    """
    from collections import deque

    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        rightmost_value = None

        for i in range(level_size):
            node = queue.popleft()
            rightmost_value = node.val   # gets overwritten each time —
                                          # ends up holding the LAST one

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(rightmost_value)

    return result


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    #        1
    #       / \
    #      2   3
    #       \    \
    #        5    4
    root = TreeNode(1,
        TreeNode(2, None, TreeNode(5)),
        TreeNode(3, None, TreeNode(4)))
    assert right_side_view(root) == [1, 3, 4]

    assert right_side_view(TreeNode(1)) == [1]
    assert right_side_view(None) == []

    # A tree where the LEFT subtree is deeper than the right —
    # the view should still correctly show left-side nodes once
    # they become the deepest (and therefore only) node at that level
    #      1
    #     /
    #    2
    #   /
    #  3
    left_heavy = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert right_side_view(left_heavy) == [1, 2, 3]

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
BFS, keep last per level:
- Time:  O(n) — same traversal as level order
- Space: O(n) — queue plus output

KEY PATTERN LEARNED:
This is a direct, minimal variation of Level Order Traversal —
worth noticing HOW small the actual change was (collecting one
value instead of a list, per level) once the underlying BFS
template is solid. The left-heavy test case above matters: it
confirms the "last node processed" trick correctly falls back to
showing a left-side node once it's the ONLY node at that depth,
which is the real intent of "right side view" even when the
tree isn't right-heavy everywhere.
"""
