"""
Problem: Kth Smallest Element in a BST
Difficulty: Medium
Category: Trees
LeetCode: #230

Problem Statement:
Given the root of a BST and an integer k, return the kth
smallest value among all node values in the tree (1-indexed).

Example:
Input:      3
           / \
          1   4
           \
            2
k = 1
Output: 1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─────────────────────────────────────────────
# APPROACH: In-order traversal, stop early at the kth value
# Time: O(h + k) | Space: O(h)
# ─────────────────────────────────────────────

def kth_smallest(root, k):
    """
    Key insight:
    An IN-ORDER traversal of a BST (left, root, right) visits
    nodes in SORTED ASCENDING ORDER — this is a defining property
    of BSTs. So the kth smallest element is simply the kth value
    encountered during an in-order traversal.

    Rather than collecting the FULL sorted list and then indexing
    into it (which wastes time/space visiting nodes beyond the
    kth if the tree is large), stop and return as soon as the
    counter reaches k.

    Example walkthrough (k=1):
          3
         / \
        1   4
         \
          2

    In-order visits: 1, 2, 3, 4 (left subtree of 3 fully first,
                                   which itself goes left(none),
                                   root(1), right(2), THEN root 3,
                                   then right subtree 4)

    count=0
    visit 1: count=1 → count == k(1) → return 1 ✅ (stops immediately,
                                                       never visits 2, 3, 4)
    """
    count = [0]
    result = [None]

    def inorder(node):
        if not node or result[0] is not None:
            return   # already found the answer — stop exploring further

        inorder(node.left)

        if result[0] is not None:
            return   # answer found while exploring left — don't continue

        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return

        inorder(node.right)

    inorder(root)
    return result[0]


# ─────────────────────────────────────────────
# ALTERNATIVE: Iterative in-order with an explicit stack
# (avoids recursion depth concerns on very unbalanced trees)
# ─────────────────────────────────────────────

def kth_smallest_iterative(root, k):
    stack = []
    current = root
    count = 0

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        count += 1

        if count == k:
            return current.val

        current = current.right

    return None


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    #        3
    #       / \
    #      1   4
    #       \
    #        2
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    assert kth_smallest(root, 1) == 1
    assert kth_smallest(root, 2) == 2
    assert kth_smallest(root, 3) == 3
    assert kth_smallest(root, 4) == 4

    assert kth_smallest_iterative(root, 1) == 1
    assert kth_smallest_iterative(root, 4) == 4

    #            5
    #           / \
    #          3   6
    #         / \
    #        2   4
    #       /
    #      1
    root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    assert kth_smallest(root2, 3) == 3

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
In-order with early stop:
- Time:  O(h + k) — in the best case, only needs to descend to
         the leftmost node (O(h)) plus visit k nodes; worst case
         still bounded well below a full O(n) traversal for small k
- Space: O(h) — recursion or explicit stack depth

KEY PATTERN LEARNED:
"In-order traversal of a BST is sorted order" is one of the most
useful BST facts to have immediately available — it turns what
looks like a search problem into a straightforward traversal
problem. The early-stop mechanism (the `result[0] is not None`
checks) matters for real efficiency, not just style — without
it, the recursion would keep exploring the entire tree even
after finding the answer, quietly turning an O(h+k) solution
into an O(n) one.
"""
