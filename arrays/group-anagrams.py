"""
Problem: Group Anagrams
Difficulty: Medium
Category: Arrays / HashMap
LeetCode: #49

Problem Statement:
Given an array of strings, group the anagrams together.
You can return the answer in any order.

Example:
Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

# ─────────────────────────────────────────────
# APPROACH: HashMap with Sorted Key
# Time: O(n * k log k) | Space: O(n * k)
# n = number of strings, k = max string length
# ─────────────────────────────────────────────

def group_anagrams(strs):
    """
    Key insight:
    Anagrams have the SAME letters, just in different order.
    If we sort each string's letters, anagrams produce
    the SAME sorted string — use this as a hashmap key!

    Example walkthrough:
    strs = ["eat","tea","tan","ate","nat","bat"]

    "eat" → sorted → "aet" → groups["aet"] = ["eat"]
    "tea" → sorted → "aet" → groups["aet"] = ["eat","tea"]
    "tan" → sorted → "ant" → groups["ant"] = ["tan"]
    "ate" → sorted → "aet" → groups["aet"] = ["eat","tea","ate"]
    "nat" → sorted → "ant" → groups["ant"] = ["tan","nat"]
    "bat" → sorted → "abt" → groups["abt"] = ["bat"]

    Result: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    """
    groups = {}

    for s in strs:
        key = "".join(sorted(s))   # sorted letters as key
        if key not in groups:
            groups[key] = []
        groups[key].append(s)

    return list(groups.values())


# ─────────────────────────────────────────────
# ALTERNATIVE: Character Count as Key (faster for long strings)
# Time: O(n * k) | Space: O(n * k)
# ─────────────────────────────────────────────

def group_anagrams_count(strs):
    from collections import defaultdict
    groups = defaultdict(list)

    for s in strs:
        # Count each letter a-z (26 count tuple as key)
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        groups[tuple(count)].append(s)

    return list(groups.values())


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    result = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    # Convert to sets for order-independent comparison
    result_sets = [set(group) for group in result]
    expected_sets = [{"eat","tea","ate"}, {"tan","nat"}, {"bat"}]

    for expected in expected_sets:
        assert expected in result_sets

    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Sorted Key Approach:
- Time:  O(n * k log k) — sort each string (k=avg length)
- Space: O(n * k) — store all strings in groups

Character Count Approach:
- Time:  O(n * k) — count chars, no sorting
- Space: O(n * k)

KEY PATTERN LEARNED:
When grouping items by some property → use HashMap with
a "canonical form" as the key. Sorted string is the canonical
form for anagrams. This pattern extends to grouping by any
transformation that's the same across a group.
"""
