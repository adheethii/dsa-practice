"""
Problem: Valid Anagram
Difficulty: Easy
Category: Strings
LeetCode: #242

Problem Statement:
Given two strings s and t, return true if t is an anagram of s,
and false otherwise.
An anagram uses all original letters exactly once.

Example:
Input:  s = "anagram", t = "nagaram"
Output: True

Input:  s = "rat", t = "car"
Output: False
"""

# ─────────────────────────────────────────────
# APPROACH 1: Sorting
# Time: O(n log n) | Space: O(n)
# ─────────────────────────────────────────────

def is_anagram_sort(s, t):
    return sorted(s) == sorted(t)


# ─────────────────────────────────────────────
# APPROACH 2: HashMap / Counter (Optimal)
# Time: O(n) | Space: O(1) — at most 26 chars
# ─────────────────────────────────────────────

def is_anagram(s, t):
    """
    Key insight:
    Count frequency of each character in both strings.
    If frequencies match → anagram!

    Example walkthrough:
    s = "anagram", t = "nagaram"

    Count s: {a:3, n:1, g:1, r:1, m:1}
    Count t: {n:1, a:3, g:1, r:1, m:1}
    Both equal → True ✅
    """
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True


# Using Python Counter (cleanest)
from collections import Counter

def is_anagram_counter(s, t):
    return Counter(s) == Counter(t)


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False
    assert is_anagram("a", "a") == True
    assert is_anagram("ab", "a") == False
    assert is_anagram("", "") == True

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Sorting:
- Time:  O(n log n)
- Space: O(n) — sorted copy

HashMap:
- Time:  O(n) — two passes
- Space: O(1) — at most 26 lowercase letters

KEY PATTERN LEARNED:
Character frequency problems → use HashMap or Counter.
Always check lengths first — different lengths = not anagram.
Counter(s) == Counter(t) is the cleanest Python solution.
"""
