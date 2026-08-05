"""
Problem: Binary Tree Maximum Path Sum
Difficulty: Hard
Category: Trees
LeetCode: #124

Problem Statement:
Given the root of a binary tree, return the maximum path sum of
any NON-EMPTY path — a path here is any sequence of nodes
connected by edges, and does NOT need to pass through the root
or end at a leaf. Unlike Path Sum, node values can be negative.

Example:
Input:      -10
            /  \
           9    20
               /  \
              15   7
Output: 42  (path: 15 -> 20 -> 7)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─────────────────────────────────────────────
# APPROACH: DFS returning "best downward path", tracking global max
# Time: O(n) | Space: O(h)
# ─────────────────────────────────────────────

def max_path_sum(root):
    """
    Key insight — this combines TWO ideas already built this
    month, Diameter of Binary Tree's "check at every node, track
    a global best" structure AND Path Sum's "carry a value down
    through recursion" idea, plus one new piece: NEGATIVE values
    change what "best" means.

    At each node, the function returns the best sum of a path
    that goes DOWNWARD from this node into at most ONE child
    (since a valid path can only continue in one direction once
    it "turns" at a node — it can't fork twice). But separately,
    at each node, we ALSO check whether a path that goes THROUGH
    this node using BOTH children (a "peak") beats the global
    best seen anywhere.

    The negative-value handling: if a child's best downward path
    is negative, including it would only HURT the total — so it's
    better to just not include that side, using max(0, ...).

    Example walkthrough:
          -10
          /  \
         9    20
             /  \
            15   7

    At node 15: no children, downward best = 15,
                through-node candidate = 15 → global_max=15
    At node 7:  no children, downward best = 7,
                through-node candidate = 7 → global_max stays 15
    At node 9:  no children, downward best = 9,
                through-node candidate = 9 → global_max stays 15
    At node 20: left downward=15, right downward=7 (both positive,
                so both kept)
                through-node candidate = 15 + 20 + 7 = 42
                → global_max = 42 ✅
                downward best returned to parent = 20 + max(15,7) = 35
    At node -10: left downward=9, right downward=35
                 negative left contribution check: max(0, 9)=9,
                 max(0, 35)=35
                 through-node candidate = 9 + (-10) + 35 = 34
                 → doesn't beat existing global_max of 42
    Final answer: 42 ✅
    """
    max_sum = [float('-inf')]

    def best_downward_path(node):
        if not node:
            return 0

        # Only include a child's contribution if it HELPS (is positive) —
        # this is the key negative-value handling
        left_gain = max(best_downward_path(node.left), 0)
        right_gain = max(best_downward_path(node.right), 0)

        # A path THROUGH this node, potentially using both children —
        # this can only be the FINAL answer, never returned upward,
        # since a path can't branch twice
        through_node = node.val + left_gain + right_gain
        max_sum[0] = max(max_sum[0], through_node)

        # What gets returned to the PARENT: this node plus at most
        # ONE side (the better one) — a valid "still extendable" path
        return node.val + max(left_gain, right_gain)

    best_downward_path(root)
    return max_sum[0]


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    #        -10
    #        /  \
    #       9    20
    #           /  \
    #          15   7
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_path_sum(root) == 42

    # Simple positive tree
    #      1
    #     / \
    #    2   3
    root2 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert max_path_sum(root2) == 6   # 2 -> 1 -> 3

    # Single negative node — the answer CAN be negative if that's
    # the only option (unlike Path Sum, negatives are allowed)
    assert max_path_sum(TreeNode(-3)) == -3

    # All negative values — best path is still just the LEAST
    # negative single node, never combining two negatives together
    root3 = TreeNode(-1, TreeNode(-2), TreeNode(-3))
    assert max_path_sum(root3) == -1

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
DFS with dual tracking (return value + side-effect global):
- Time:  O(n) — one pass
- Space: O(h) — recursion stack

KEY PATTERN LEARNED:
Worth being explicit about the distinction this problem forces:
the value RETURNED from the recursive call (best single-direction
downward path, usable by a parent) is DIFFERENT from the value
tracked as the answer (best through-node path, using both sides,
which can never be extended further and so is never returned
upward). Conflating these two — trying to return the through-node
sum to the parent — is the single most common bug in this
problem, and is exactly what the "all negative values" test case
is designed to catch, since combining two negative branches
together would incorrectly beat a single least-negative node.
"""
