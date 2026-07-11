"""
Problem: Reverse Linked List
Difficulty: Easy
Category: Linked Lists
LeetCode: #206

Problem Statement:
Given the head of a singly linked list, reverse the list
and return the new head.

Example:
Input:  1 → 2 → 3 → 4 → 5
Output: 5 → 4 → 3 → 2 → 1
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
# APPROACH 1: Iterative (Optimal)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────

def reverse_list(head):
    """
    Key insight:
    Keep track of previous node. For each node,
    flip its 'next' pointer to point backward instead of forward.

    Example walkthrough:
    1 → 2 → 3 → None

    prev=None, curr=1
    step1: next_temp=2, 1.next=None, prev=1, curr=2
           → None ← 1    2 → 3

    step2: next_temp=3, 2.next=1, prev=2, curr=3
           → None ← 1 ← 2    3

    step3: next_temp=None, 3.next=2, prev=3, curr=None
           → None ← 1 ← 2 ← 3

    return prev (which is 3, the new head)
    """
    prev = None
    curr = head

    while curr:
        next_temp = curr.next   # save next node before overwriting
        curr.next = prev        # reverse the pointer
        prev = curr             # move prev forward
        curr = next_temp        # move curr forward

    return prev   # prev is now the new head


# ─────────────────────────────────────────────
# APPROACH 2: Recursive
# Time: O(n) | Space: O(n) — call stack
# ─────────────────────────────────────────────

def reverse_list_recursive(head):
    if not head or not head.next:
        return head

    new_head = reverse_list_recursive(head.next)
    head.next.next = head   # reverse the pointer
    head.next = None

    return new_head


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
    head = make_list([1, 2, 3, 4, 5])
    reversed_head = reverse_list(head)
    assert reversed_head.to_list() == [5, 4, 3, 2, 1]

    head = make_list([1, 2])
    reversed_head = reverse_list(head)
    assert reversed_head.to_list() == [2, 1]

    head = make_list([])
    assert reverse_list(head) is None

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Iterative:
- Time:  O(n) — visit each node once
- Space: O(1) — only three pointers

KEY PATTERN LEARNED:
The three-pointer technique (prev, curr, next_temp) is
THE fundamental pattern for linked list reversal.
Always save next BEFORE modifying curr.next.
This exact pattern is asked in almost every technical interview!
"""
