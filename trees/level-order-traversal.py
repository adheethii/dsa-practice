"""
Problem: Binary Tree Level Order Traversal
Difficulty: Medium
Category: Trees / BFS
LeetCode: #102

Problem Statement:
Given the root of a binary tree, return the level order
traversal of its nodes' values — grouped by level, left to right.

Example:
Input:      3
           / \
          9  20
             /  \
            15   7
Output: [[3],[9,20],[15,7]]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─────────────────────────────────────────────
# APPROACH: BFS, processing one full level at a time
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────

def level_order(root):
    """
    Key insight:
    This is the SAME "level_size snapshot" technique used in
    Rotting Oranges and Maximum Depth's BFS variant earlier this
    month — capture len(queue) BEFORE the inner loop starts, so
    the inner loop processes EXACTLY that many nodes (one full
    level), even though new nodes get added to the same queue
    during that loop.

    Example walkthrough:
          3
         / \
        9  20
           /  \
          15   7

    queue=[3], level_size=1
      pop 3, add to current_level=[3], push 9 and 20
    result=[[3]], queue=[9,20]

    queue=[9,20], level_size=2 (snapshotted BEFORE processing)
      pop 9, add to current_level=[9], no children to push
      pop 20, add to current_level=[9,20], push 15 and 7
    result=[[3],[9,20]], queue=[15,7]

    queue=[15,7], level_size=2
      pop 15, pop 7, add both to current_level=[15,7]
    result=[[3],[9,20],[15,7]] ✅
    """
    from collections import deque

    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)   # snapshot — how many nodes are in THIS level
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    #        3
    #       / \
    #      9  20
    #         /  \
    #        15   7
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(root) == [[3], [9, 20], [15, 7]]

    assert level_order(TreeNode(1)) == [[1]]
    assert level_order(None) == []

    # Skewed tree — every level has exactly one node
    skewed = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert level_order(skewed) == [[1], [2], [3]]

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
BFS with level snapshotting:
- Time:  O(n) — every node visited exactly once
- Space: O(n) — the queue can hold up to n/2 nodes at the widest
         level, plus the output storage

KEY PATTERN LEARNED:
The "snapshot len(queue) before the inner loop" trick is worth
recognizing as a REUSABLE technique now that it's shown up three
times this month (Rotting Oranges' minute-by-minute spread,
Maximum Depth's BFS variant, and here) — it's the standard way
to process a graph or tree "layer by layer" using a single
queue, without needing two separate queues or extra bookkeeping.
"""
