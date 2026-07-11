"""
Problem: Valid Parentheses
Difficulty: Easy
Category: Stacks
LeetCode: #20

Problem Statement:
Given a string containing '(', ')', '{', '}', '[', ']',
determine if the input string is valid.
A string is valid if brackets are closed in the correct order.

Example:
Input:  s = "()[]{}"
Output: True

Input:  s = "(]"
Output: False
"""

# ─────────────────────────────────────────────
# APPROACH: Stack (Optimal)
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────

def is_valid(s):
    """
    Key insight:
    Use a stack to track opening brackets.
    When we see a closing bracket, check if it matches
    the most recent opening bracket (top of stack).

    Example walkthrough:
    s = "{[()]}"

    '{' → push → stack=['{']
    '[' → push → stack=['{','[']
    '(' → push → stack=['{','[','(']
    ')' → matches '(' → pop → stack=['{','[']
    ']' → matches '[' → pop → stack=['{']
    '}' → matches '{' → pop → stack=[]
    stack empty → VALID! ✅
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0   # valid only if all brackets matched


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert is_valid("()") == True
    assert is_valid("()[]{}")== True
    assert is_valid("(]") == False
    assert is_valid("([)]") == False
    assert is_valid("{[]}") == True
    assert is_valid("(") == False
    assert is_valid("") == True

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Stack Approach:
- Time:  O(n) — single pass through string
- Space: O(n) — stack can hold up to n/2 opening brackets

KEY PATTERN LEARNED:
Stack is THE data structure for matching/nesting problems.
Pattern: push opening symbols, pop and check on closing symbols.
This pattern extends to: balanced XML/HTML tags, expression evaluation,
undo/redo functionality.
"""
