"""
Problem: Maximum Depth of Binary Tree
Difficulty: Easy
Category: Trees
LeetCode: #104

Problem Statement:
Given the root of a binary tree, return its maximum depth — the
number of nodes along the longest path from root to the farthest
leaf node.

Example:
Input:      3
           / \
          9  20
             /  \
            15   7
Output: 3
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─────────────────────────────────────────────
# APPROACH: Recursive DFS
# Time: O(n) | Space: O(h) — h = tree height
# ─────────────────────────────────────────────

def max_depth(root):
    """
    Key insight:
    The depth of a tree rooted at any node is 1 (for the node
    itself) plus the LARGER of its two subtrees' depths. This
    recursive definition maps directly onto the code — an empty
    tree has depth 0, everything else builds up from there.

    Example walkthrough:
          3
         / \
        9  20
           /  \
          15   7

    max_depth(3) = 1 + max(max_depth(9), max_depth(20))
      max_depth(9) = 1 + max(max_depth(None), max_depth(None))
                   = 1 + max(0, 0) = 1
      max_depth(20) = 1 + max(max_depth(15), max_depth(7))
                    = 1 + max(1, 1) = 2
    max_depth(3) = 1 + max(1, 2) = 3 ✅
    """
    if not root:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)


# ─────────────────────────────────────────────
# APPROACH 2: Iterative BFS (level by level)
# Time: O(n) | Space: O(n) worst case — widest level
# ─────────────────────────────────────────────

def max_depth_bfs(root):
    """Count levels by processing the tree one full level at a time."""
    from collections import deque

    if not root:
        return 0

    queue = deque([root])
    depth = 0

    while queue:
        depth += 1
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth


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
    assert max_depth(root) == 3
    assert max_depth_bfs(root) == 3

    assert max_depth(None) == 0
    assert max_depth(TreeNode(1)) == 1

    # Skewed tree (essentially a linked list) — depth = 3
    skewed = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert max_depth(skewed) == 3

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Recursive DFS:
- Time:  O(n) — visits every node exactly once
- Space: O(h) — recursion stack depth equals tree height
         (O(log n) for a balanced tree, O(n) for a skewed one)

Iterative BFS:
- Time:  O(n)
- Space: O(n) worst case — the queue can hold an entire level,
         which for a wide/balanced tree can be up to n/2 nodes

KEY PATTERN LEARNED:
This is the simplest possible tree recursion, and worth treating
as the TEMPLATE for tree problems generally: handle the None
base case first, recurse on left and right, then COMBINE the
two results at the current node. Nearly every tree problem
(Validate BST from earlier, and the two path-based problems in
this same batch) follows this exact recurse-then-combine shape,
just with a different combination step.
"""
