"""
Problem: Valid Palindrome
Difficulty: Easy
Category: Strings
LeetCode: #125

Problem Statement:
A phrase is a palindrome if, after converting all uppercase letters to lowercase
and removing all non-alphanumeric characters, it reads the same forward and backward.
Return true if s is a palindrome, false otherwise.

Example:
Input:  s = "A man, a plan, a canal: Panama"
Output: True  ("amanaplanacanalpanama" is a palindrome)

Input:  s = "race a car"
Output: False  ("raceacar" is not a palindrome)
"""

# ─────────────────────────────────────────────
# APPROACH 1: Clean then check
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────

def is_palindrome_clean(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]


# ─────────────────────────────────────────────
# APPROACH 2: Two Pointers (Optimal)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────

def is_palindrome(s):
    """
    Key insight:
    Use two pointers — skip non-alphanumeric characters.
    Compare characters from both ends moving inward.

    Example walkthrough:
    s = "A man, a plan, a canal: Panama"

    left=0 'A', right=29 'a' → both alpha → lower → 'a'=='a' ✅ → move inward
    left=1 ' ', → skip (not alnum) → left=2 'm'
    right=28 'm' → 'm'=='m' ✅ → move inward
    ... continue until left >= right → palindrome!
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome(" ") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("hello") == False

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Approach 1 (Clean + reverse):
- Time:  O(n) — clean + compare
- Space: O(n) — cleaned list

Approach 2 (Two Pointers):
- Time:  O(n) — single pass
- Space: O(1) — only two pointers ✅ optimal

KEY PATTERN LEARNED:
Two pointers from both ends is the go-to for palindrome problems.
Always handle edge cases: non-alphanumeric chars, case sensitivity.
isalnum() checks if character is letter or digit.
"""
