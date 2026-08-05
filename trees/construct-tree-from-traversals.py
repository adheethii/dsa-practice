"""
Problem: Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium
Category: Trees
LeetCode: #105

Problem Statement:
Given two integer arrays preorder and inorder, where preorder is
the preorder traversal of a binary tree and inorder is the
inorder traversal of the SAME tree, construct and return the
original binary tree. Assumes no duplicate values.

Example:
Input:  preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: the tree      3
                      / \
                     9  20
                        /  \
                       15   7
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─────────────────────────────────────────────
# APPROACH: Recursive split using preorder's first element as root
# Time: O(n) with hashmap | Space: O(n)
# ─────────────────────────────────────────────

def build_tree(preorder, inorder):
    """
    Key insight:
    Two facts about these traversal orders combine to make this
    solvable:

    1. PREORDER always visits the ROOT first, then left subtree,
       then right subtree. So preorder[0] is ALWAYS the root of
       whatever subtree is currently being built.

    2. INORDER visits left subtree, then root, then right
       subtree. So once we know the root's VALUE, its position
       in inorder tells us exactly how many nodes belong to the
       left subtree (everything before it) versus the right
       subtree (everything after it).

    Combining these: find the root from preorder[0], locate it in
    inorder to split the tree into left/right portions, then
    recurse on each portion using the CORRESPONDING slice of
    preorder.

    Example walkthrough:
    preorder = [3,9,20,15,7]
    inorder  = [9,3,15,20,7]

    root = preorder[0] = 3
    find 3 in inorder → index 1
      → left subtree has 1 node (everything before index 1): [9]
      → right subtree has 3 nodes (everything after): [15,20,7]

    left subtree's preorder slice: preorder[1 : 1+1] = [9]
    right subtree's preorder slice: preorder[1+1 :] = [20,15,7]

    Recurse left:  preorder=[9], inorder=[9] → single node, root=9
    Recurse right: preorder=[20,15,7], inorder=[15,20,7]
      root=20, find 20 in inorder → index 1
      → left has [15], right has [7]
      ...builds out 20's children correctly
    """
    if not preorder or not inorder:
        return None

    # Map value -> index in inorder, for O(1) lookups instead of
    # re-scanning inorder with .index() on every recursive call
    inorder_index = {val: i for i, val in enumerate(inorder)}

    def helper(pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end:
            return None

        root_val = preorder[pre_start]
        root = TreeNode(root_val)

        root_index_in_inorder = inorder_index[root_val]
        left_size = root_index_in_inorder - in_start

        root.left = helper(
            pre_start + 1, pre_start + left_size,
            in_start, root_index_in_inorder - 1
        )
        root.right = helper(
            pre_start + left_size + 1, pre_end,
            root_index_in_inorder + 1, in_end
        )

        return root

    return helper(0, len(preorder) - 1, 0, len(inorder) - 1)


def tree_to_preorder(root):
    """Helper for tests — convert a tree back to preorder to verify."""
    if not root:
        return []
    return [root.val] + tree_to_preorder(root.left) + tree_to_preorder(root.right)


def tree_to_inorder(root):
    """Helper for tests — convert a tree back to inorder to verify."""
    if not root:
        return []
    return tree_to_inorder(root.left) + [root.val] + tree_to_inorder(root.right)


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    root = build_tree(preorder, inorder)

    # Verify by converting the built tree back to both traversal
    # orders and checking they match the original inputs exactly
    assert tree_to_preorder(root) == preorder
    assert tree_to_inorder(root) == inorder

    # Also verify the actual structure directly
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    assert root.right.left.val == 15
    assert root.right.right.val == 7

    assert build_tree([], []) is None
    assert build_tree([1], [1]).val == 1

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Recursive split with hashmap lookup:
- Time:  O(n) — with the hashmap, each node is processed in O(1)
         beyond the recursive calls (without the hashmap, using
         inorder.index() instead, this degrades to O(n^2))
- Space: O(n) — hashmap plus recursion stack

KEY PATTERN LEARNED:
This is the first "construction" problem in the trees set today,
distinct from traversal or comparison — it goes the OTHER
direction, from traversal orders BACK into a tree structure. The
hashmap-for-index-lookup optimization is worth remembering
specifically: it's an easy thing to skip in a first attempt,
and is exactly what separates an O(n) solution from an O(n^2) one
here.
"""
