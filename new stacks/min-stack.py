"""
Problem: Min Stack
Difficulty: Medium
Category: Stacks
LeetCode: #155

Problem Statement:
Design a stack that supports push, pop, top, and retrieving
the minimum element — all in O(1) time.

Example:
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin() → -3
minStack.pop()
minStack.top()     → 0
minStack.getMin()  → -2
"""

# ─────────────────────────────────────────────
# APPROACH: Two Stacks (Optimal)
# Time: O(1) all operations | Space: O(n)
# ─────────────────────────────────────────────

class MinStack:
    """
    Key insight:
    Maintain a SECOND stack that tracks the minimum
    at each point in time — parallel to the main stack.

    Example walkthrough:
    push(-2): stack=[-2],      min_stack=[-2]
    push(0):  stack=[-2,0],    min_stack=[-2,-2]  (min unchanged)
    push(-3): stack=[-2,0,-3], min_stack=[-2,-2,-3] (new min!)

    getMin() → min_stack[-1] = -3 ✅

    pop(): stack=[-2,0], min_stack=[-2,-2]
    getMin() → min_stack[-1] = -2 ✅ (back to previous min!)
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push to min_stack — either new min or repeat current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)

    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Two Stacks:
- Time:  O(1) — for push, pop, top, getMin
- Space: O(n) — two stacks of same size

KEY PATTERN LEARNED:
When you need O(1) access to "extra info" (min, max, etc.)
alongside normal stack operations — maintain a PARALLEL stack
that tracks that info at each state.
This pattern extends to: Max Stack, Stack with running average.
"""
