"""
Problem: Delete Node in a BST
Difficulty: Medium
Category: Trees / BST
LeetCode: #450

Problem Statement:
Given the root of a BST and a key, delete the node with that key
value and return the new root, maintaining the BST property.

Example:
Input:  root = [5,3,6,2,4,None,7], key = 3
Output: any valid BST missing the value 3
        (e.g. [4,2,6,None,None,5,7] or several other valid results)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_sorted_list(self):
        result = []
        if self.left:
            result += self.left.to_sorted_list()
        result.append(self.val)
        if self.right:
            result += self.right.to_sorted_list()
        return result


# ─────────────────────────────────────────────
# APPROACH: Recursive, three cases based on node's children
# Time: O(h) | Space: O(h)
# ─────────────────────────────────────────────

def delete_node(root, key):
    r"""
    Key insight — this is genuinely harder than Insert, because
    there are THREE distinct cases once the target node is found:

    Case 1: Node has NO children (leaf) → just remove it (return None)

    Case 2: Node has ONE child → replace the node with that child
            (the child "moves up" to take the deleted node's place)

    Case 3: Node has TWO children → this is the hard case. Can't
            just remove it without breaking BST ordering on both
            sides. Instead: find the node's IN-ORDER SUCCESSOR
            (the smallest value in the right subtree — guaranteed
            to be larger than everything on the left, smaller than
            everything else on the right), copy that value into
            the current node, then recursively delete the successor
            from the right subtree (which will hit Case 1 or 2,
            never Case 3 again, since the successor has no left child)

    Example walkthrough — deleting 3 from:
          5
         / \
        3   6
       / \    \
      2   4    7

    Found node 3, has TWO children (2 and 4).
    In-order successor of 3 = smallest value in its right subtree
    = 4 (4 has no left child, so it IS the smallest there)
    Copy 4's value into node 3's position → node becomes "4"
    Recursively delete the ORIGINAL 4 from the right subtree
    (that 4 is a leaf → Case 1, just remove it)

    Result:
          5
         / \
        4   6
       /      \
      2        7
    """
    if not root:
        return None

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # Found the node to delete
        if not root.left:
            return root.right    # Case 1 (no children) or Case 2 (only right child)
        if not root.right:
            return root.left     # Case 2 (only left child)

        # Case 3: two children — find in-order successor
        successor = root.right
        while successor.left:
            successor = successor.left

        root.val = successor.val   # copy successor's value into this node
        root.right = delete_node(root.right, successor.val)   # remove the duplicate

    return root


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    #      5
    #     / \
    #    3   6
    #   / \    \
    #  2   4    7
    def build_tree():
        return TreeNode(5,
                         TreeNode(3, TreeNode(2), TreeNode(4)),
                         TreeNode(6, None, TreeNode(7)))

    # Delete a node with two children
    root = build_tree()
    result = delete_node(root, 3)
    assert 3 not in result.to_sorted_list()
    assert result.to_sorted_list() == [2, 4, 5, 6, 7]   # still fully sorted -> valid BST

    # Delete a leaf node
    root = build_tree()
    result = delete_node(root, 2)
    assert result.to_sorted_list() == [3, 4, 5, 6, 7]

    # Delete a node with only one child
    root = build_tree()
    result = delete_node(root, 6)   # 6 has only a right child (7)
    assert result.to_sorted_list() == [2, 3, 4, 5, 7]

    # Delete a key that doesn't exist — tree unchanged
    root = build_tree()
    result = delete_node(root, 100)
    assert result.to_sorted_list() == [2, 3, 4, 5, 6, 7]

    # Delete from an empty tree
    assert delete_node(None, 5) is None

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Recursive BST deletion:
- Time:  O(h) — one pass down to find the node, plus at most
         another O(h) to find the in-order successor in Case 3
- Space: O(h) — recursion stack

KEY PATTERN LEARNED:
This is the problem where BST deletion earns its "genuinely
harder" reputation — Case 3 (two children) is the one worth
being able to reconstruct from memory in an interview, not just
recognize. The in-order-successor trick (smallest value in the
right subtree) is the standard solution; an equally valid
alternative is using the in-order PREDECESSOR (largest value in
the left subtree) instead — both work, pick one and be consistent.
"""
