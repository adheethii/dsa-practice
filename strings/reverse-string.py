"""
Problem: Reverse String
Difficulty: Easy
Category: Strings
LeetCode: #344

Problem Statement:
Write a function that reverses a string.
The input is given as an array of characters s.
You must do this in-place with O(1) extra memory.

Example:
Input:  s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input:  s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

# ─────────────────────────────────────────────
# APPROACH: Two Pointers (In-place)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────

def reverse_string(s):
    """
    Key insight:
    Use two pointers — one at start, one at end.
    Swap characters and move pointers inward.
    Stop when pointers meet in the middle.

    Example walkthrough:
    s = ["h","e","l","l","o"]

    left=0, right=4 → swap h,o → ["o","e","l","l","h"]
    left=1, right=3 → swap e,l → ["o","l","l","e","h"]
    left=2, right=2 → left >= right → STOP ✅
    """
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]   # swap
        left += 1
        right -= 1


# ─────────────────────────────────────────────
# BONUS: Reverse a string (not in-place)
# ─────────────────────────────────────────────

def reverse_string_simple(s):
    # Python slicing — not in-place but clean
    return s[::-1]

def reverse_words(sentence):
    # Reverse words in a sentence
    return " ".join(sentence.split()[::-1])


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # Test 1
    s = ["h","e","l","l","o"]
    reverse_string(s)
    assert s == ["o","l","l","e","h"]

    # Test 2
    s = ["H","a","n","n","a","h"]
    reverse_string(s)
    assert s == ["h","a","n","n","a","H"]

    # Test 3 — single character
    s = ["a"]
    reverse_string(s)
    assert s == ["a"]

    # Test 4 — two characters
    s = ["a","b"]
    reverse_string(s)
    assert s == ["b","a"]

    # Bonus tests
    assert reverse_string_simple("hello") == "olleh"
    assert reverse_words("I love Python") == "Python love I"

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Two Pointers (in-place):
- Time:  O(n) — visit each character once
- Space: O(1) — only two pointer variables

Python slicing s[::-1]:
- Time:  O(n)
- Space: O(n) — creates new string

KEY PATTERN LEARNED:
Two pointers is perfect for in-place array/string operations.
Start from both ends and work inward.
Common use: reverse, palindrome check, remove duplicates.
"""
