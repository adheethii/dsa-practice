"""
Problem: Number of Islands
Difficulty: Medium
Category: Graphs / BFS / DFS
LeetCode: #200

Problem Statement:
Given an m x n 2D binary grid representing land ('1') and water ('0'),
return the number of islands. An island is surrounded by water and
formed by connecting adjacent lands horizontally or vertically.

Example:
Input:
[["1","1","0","0","0"],
 ["1","1","0","0","0"],
 ["0","0","1","0","0"],
 ["0","0","0","1","1"]]
Output: 3
"""

# ─────────────────────────────────────────────
# APPROACH: DFS (Flood Fill)
# Time: O(m*n) | Space: O(m*n) worst case (recursion stack)
# ─────────────────────────────────────────────

def num_islands(grid):
    """
    Key insight:
    For each unvisited '1', do a DFS to "sink" the entire island
    (mark all connected land as visited). Count how many times
    we START a new DFS — that's the number of islands.

    Example walkthrough:
    Find first '1' at (0,0) → DFS marks all connected land as '0'
    → island count = 1
    Continue scanning → find '1' at (2,2) → DFS marks it
    → island count = 2
    Find '1' at (3,3) → DFS marks connected (3,3),(3,4)
    → island count = 3
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r, c):
        # Base cases: out of bounds or water/visited
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return

        grid[r][c] = "0"   # mark as visited (sink it)

        # Explore all 4 directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)   # sink entire connected island

    return islands


# ─────────────────────────────────────────────
# APPROACH 2: BFS (avoids recursion depth issues)
# Time: O(m*n) | Space: O(min(m,n))
# ─────────────────────────────────────────────

def num_islands_bfs(grid):
    from collections import deque

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = "0"

        while queue:
            row, col = queue.popleft()
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                bfs(r, c)

    return islands


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    grid1 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert num_islands([row[:] for row in grid1]) == 3

    grid2 = [
        ["1","1","1"],
        ["0","1","0"],
        ["1","0","1"]
    ]
    assert num_islands([row[:] for row in grid2]) == 3

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
DFS/BFS Flood Fill:
- Time:  O(m*n) — visit every cell at most once
- Space: O(m*n) worst case for DFS recursion stack (all land)
         O(min(m,n)) for BFS queue

KEY PATTERN LEARNED:
"Flood fill" is THE pattern for counting connected components in a grid.
Start DFS/BFS from each unvisited land cell, mark everything connected
as visited, count how many times you START a new search.
This pattern extends to: Number of Provinces, Max Area of Island,
Surrounded Regions.
"""
