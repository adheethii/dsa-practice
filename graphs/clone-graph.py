"""
Problem: Clone Graph
Difficulty: Medium
Category: Graphs / DFS
LeetCode: #133

Problem Statement:
Given a reference node in a connected undirected graph, return
a DEEP COPY (clone) of the graph. Each node has a value and a
list of neighbors.

Example:
Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: A completely separate graph with the same structure/values
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# ─────────────────────────────────────────────
# APPROACH: DFS with a Visited HashMap
# Time: O(V + E) | Space: O(V)
# ─────────────────────────────────────────────

def clone_graph(node):
    """
    Key insight:
    The graph may have CYCLES (it's undirected — A points to B,
    B points back to A). A naive DFS would infinite-loop cloning
    the same nodes forever.

    The fix: keep a HashMap of {original_node: cloned_node}.
    Before cloning a node's neighbors, check if it's ALREADY
    been cloned — if so, reuse that clone instead of recursing
    again. This is what breaks the infinite cycle.

    Example walkthrough:
    Original: 1 -- 2
              |    |
              4 -- 3

    clone(1): not in map, create clone_1, map={1: clone_1}
      for neighbor 2: clone(2)
        not in map, create clone_2, map={1:clone_1, 2:clone_2}
        for neighbor 1: clone(1)
          ALREADY in map! return clone_1 (no infinite loop)
        for neighbor 3: clone(3)... and so on
    """
    if not node:
        return None

    visited = {}   # original node -> its clone

    def dfs(original):
        if original in visited:
            return visited[original]   # already cloned — reuse it!

        # Create the clone BEFORE recursing into neighbors —
        # this is what prevents infinite recursion on cycles
        clone = Node(original.val)
        visited[original] = clone

        for neighbor in original.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # Build a small graph: 1 -- 2, 1 -- 4, 2 -- 3, 3 -- 4 (a 4-cycle)
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    cloned = clone_graph(n1)

    assert cloned is not n1                       # different object (deep copy)
    assert cloned.val == 1
    assert len(cloned.neighbors) == 2
    assert cloned.neighbors[0] is not n2           # neighbors are also cloned
    assert cloned.neighbors[0].val == 2

    # No infinite loop occurred, and structure is preserved
    assert clone_graph(None) is None

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
DFS with visited map:
- Time:  O(V + E) — visit every node and every edge once
- Space: O(V) — the visited hashmap stores one entry per node

KEY PATTERN LEARNED:
"Clone/copy a graph with possible cycles" ALWAYS needs a
visited/seen map keyed by the ORIGINAL node, mapping to its
clone. Create the clone entry in the map BEFORE recursing into
neighbors — if you create it AFTER, cycles will still cause
infinite recursion. This exact ordering detail is a common
subtle bug.
"""
