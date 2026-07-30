"""
Problem: Implement Trie (Prefix Tree)
Difficulty: Medium
Category: Design / Strings / Trees
LeetCode: #208

Problem Statement:
Implement a Trie with insert, search, and startsWith methods.
A Trie efficiently stores and searches strings by shared prefixes.

Example:
trie.insert("apple")
trie.search("apple")   → True
trie.search("app")     → False (not inserted as a complete word)
trie.startsWith("app") → True (prefix exists)
"""

# ─────────────────────────────────────────────
# APPROACH: Tree of nested dictionaries
# Time: O(L) per operation, L = word length | Space: O(total characters)
# ─────────────────────────────────────────────

class TrieNode:
    def __init__(self):
        self.children = {}     # char -> TrieNode
        self.is_end_of_word = False


class Trie:
    """
    Key insight:
    Each node represents ONE character. A path from root to a
    node spells out a prefix. is_end_of_word marks nodes where
    a COMPLETE word ends (not just a prefix).

    Example: inserting "app" and "apple"

    root
     └─ a
         └─ p
             └─ p (is_end_of_word=True, since "app" was inserted)
                 └─ l
                     └─ e (is_end_of_word=True, "apple" inserted)

    Both "app" and "apple" share the same "a-p-p" path — this
    sharing is what makes Tries memory-efficient for many words
    with common prefixes.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str):
        """Walk the trie following prefix; return the final node or None."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")

    assert trie.search("apple") == True
    assert trie.search("app") == False       # "app" never inserted as a full word
    assert trie.startsWith("app") == True    # but it IS a valid prefix
    assert trie.search("appl") == False
    assert trie.startsWith("appl") == True

    trie.insert("app")
    assert trie.search("app") == True        # now it's a complete word too

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Trie:
- Insert:      O(L) — L = length of word
- Search:      O(L)
- startsWith:  O(L)
- Space:       O(total characters across all inserted words),
               with SHARED prefixes stored only once

KEY PATTERN LEARNED:
Tries beat storing words in a plain hash set whenever PREFIX
queries matter (autocomplete, spell-check, IP routing tables).
A hash set can do search() in O(1) but CANNOT efficiently answer
"does any word start with this prefix?" — that requires scanning
every word. Tries answer both in O(L), independent of how many
words are stored.
"""
