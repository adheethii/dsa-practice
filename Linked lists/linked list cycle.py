"""
Problem: Linked List Cycle
Difficulty: Easy
Category: Linked Lists
LeetCode: #141

Problem Statement:
Given the head of a linked list, determine if the list has a cycle.
A cycle exists if some node can be reached again by following next pointers.

Example:
Input:  3 → 2 → 0 → -4 → (back to 2)
Output: True

Input:  1 → 2 → None
Output: False
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ─────────────────────────────────────────────
# APPROACH 1: HashSet
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────

def has_cycle_set(head):
    seen = set()
    current = head
    while current:
        if id(current) in seen:
            return True
        seen.add(id(current))
        current = current.next
    return False


# ─────────────────────────────────────────────
# APPROACH 2: Floyd's Cycle Detection (Optimal)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────

def has_cycle(head):
    """
    Key insight — Floyd's Tortoise and Hare:
    Use two pointers — slow (1 step) and fast (2 steps).
    If there's a cycle, fast will eventually catch up to slow.
    If no cycle, fast reaches None.

    Analogy: Runner on a circular track — faster runner
    laps the slower one eventually.
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # 1 step
        fast = fast.next.next     # 2 steps

        if slow == fast:          # they met → cycle exists!
            return True

    return False                  # fast reached end → no cycle


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # Test 1 — cycle exists
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2   # cycle back to n2
    assert has_cycle(n1) == True

    # Test 2 — no cycle
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    assert has_cycle(n1) == False

    # Test 3 — single node no cycle
    n1 = ListNode(1)
    assert has_cycle(n1) == False

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Floyd's Algorithm:
- Time:  O(n) — fast pointer traverses at most 2n steps
- Space: O(1) — only two pointers

KEY PATTERN LEARNED:
Floyd's cycle detection = two pointers at different speeds.
Fast pointer moves 2x speed of slow pointer.
If cycle exists → they will ALWAYS meet.
This pattern applies to: cycle detection, finding middle node,
finding cycle start point.
"""
