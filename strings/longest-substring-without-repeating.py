"""
Problem: Longest Substring Without Repeating Characters
Difficulty: Medium
Category: Strings / Sliding Window
LeetCode: #3

Problem Statement:
Given a string s, find the length of the longest substring
without repeating characters.

Example:
Input:  s = "abcabcbb"
Output: 3  ("abc")

Input:  s = "pwwkew"
Output: 3  ("wke")
"""

# ─────────────────────────────────────────────
# APPROACH: Sliding Window with HashMap
# Time: O(n) | Space: O(min(n, charset_size))
# ─────────────────────────────────────────────

def length_of_longest_substring(s):
    """
    Key insight:
    Maintain a "window" [left, right] that always contains
    unique characters. Expand right; when a duplicate is found,
    shrink from the left until the duplicate is removed.

    Example walkthrough:
    s = "abcabcbb"

    right=0 'a': window="a",    max_len=1
    right=1 'b': window="ab",   max_len=2
    right=2 'c': window="abc",  max_len=3
    right=3 'a': DUPLICATE! move left past first 'a'
                 window="bca",  max_len=3
    right=4 'b': DUPLICATE! move left past 'b'
                 window="cab",  max_len=3
    right=5 'c': DUPLICATE! move left past 'c'
                 window="abc",  max_len=3
    right=6 'b': DUPLICATE! move left
                 window="cb",   max_len=3
    right=7 'b': DUPLICATE!
                 window="b",    max_len=3

    Final answer: 3
    """
    char_index = {}   # char -> most recent index seen
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            # Duplicate found within current window — shrink from left
            left = char_index[char] + 1

        char_index[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring(" ") == 1
    assert length_of_longest_substring("dvdf") == 3

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Sliding Window:
- Time:  O(n) — each character visited at most twice (once by right, once by left)
- Space: O(min(n, charset)) — hashmap stores at most charset_size entries

KEY PATTERN LEARNED:
Sliding Window is THE pattern for substring/subarray problems with
a constraint (no duplicates, sum ≤ target, etc.). Expand right pointer
to grow the window, shrink left pointer when constraint is violated.
Track the answer at each valid window state.
This exact pattern appears constantly in technical interviews.
"""
