"""
Problem: Merge Two Sorted Lists
Difficulty: Easy
Category: Linked Lists
LeetCode: #21

Problem Statement:
Merge two sorted linked lists and return it as a sorted list.

Example:
Input:  l1 = 1→2→4, l2 = 1→3→4
Output: 1→1→2→3→4→4
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self):
        result = []
        curr = self
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result


# ─────────────────────────────────────────────
# APPROACH 1: Iterative (with dummy node)
# Time: O(m+n) | Space: O(1)
# ─────────────────────────────────────────────

def merge_two_lists(l1, l2):
    """
    Key insight:
    Use a dummy node to simplify edge cases.
    Compare heads of both lists, attach the smaller one.
    Attach remaining list at the end.

    Example walkthrough:
    l1: 1→2→4
    l2: 1→3→4

    dummy → compare 1,1 → attach l1's 1 → dummy→1
    compare 2,1 → attach l2's 1 → dummy→1→1
    compare 2,3 → attach l1's 2 → dummy→1→1→2
    compare 4,3 → attach l2's 3 → dummy→1→1→2→3
    compare 4,4 → attach l1's 4 → dummy→1→1→2→3→4
    l1 exhausted → attach remaining l2 → dummy→1→1→2→3→4→4
    """
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach remaining list
    current.next = l1 if l1 else l2

    return dummy.next


# ─────────────────────────────────────────────
# APPROACH 2: Recursive
# Time: O(m+n) | Space: O(m+n) — call stack
# ─────────────────────────────────────────────

def merge_two_lists_recursive(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val <= l2.val:
        l1.next = merge_two_lists_recursive(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists_recursive(l1, l2.next)
        return l2


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

def make_list(vals):
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


if __name__ == "__main__":
    l1 = make_list([1, 2, 4])
    l2 = make_list([1, 3, 4])
    result = merge_two_lists(l1, l2)
    assert result.to_list() == [1, 1, 2, 3, 4, 4]

    l1 = make_list([])
    l2 = make_list([])
    assert merge_two_lists(l1, l2) is None

    l1 = make_list([])
    l2 = make_list([0])
    result = merge_two_lists(l1, l2)
    assert result.to_list() == [0]

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Iterative:
- Time:  O(m+n) — visit each node once
- Space: O(1) — dummy node trick, no extra space

KEY PATTERN LEARNED:
Dummy node is the go-to trick for linked list problems.
It eliminates edge cases for empty lists or head changes.
Pattern: create dummy → build list → return dummy.next
"""
