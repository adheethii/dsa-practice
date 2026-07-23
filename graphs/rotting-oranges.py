"""
Problem: Rotting Oranges
Difficulty: Medium
Category: Graphs / BFS (Multi-source)
LeetCode: #994

Problem Statement:
Grid where 0=empty, 1=fresh orange, 2=rotten orange. Every minute,
a rotten orange rots adjacent fresh oranges. Return the minimum
minutes until no fresh orange remains, or -1 if impossible.

Example:
Input:
[[2,1,1],
 [1,1,0],
 [0,1,1]]
Output: 4
"""

# ─────────────────────────────────────────────
# APPROACH: Multi-source BFS
# Time: O(m*n) | Space: O(m*n)
# ─────────────────────────────────────────────

def oranges_rotting(grid):
    """
    Key insight:
    This is a "multi-source" BFS — start the BFS from ALL rotten
    oranges SIMULTANEOUSLY (not one at a time), since they all
    rot their neighbors in the same minute in parallel.

    Example walkthrough:
    Minute 0: rotten oranges at (0,0). Fresh oranges elsewhere.
    Minute 1: (0,0) rots its neighbors (0,1) and (1,0)
    Minute 2: those rot THEIR neighbors
    ...continue until queue empties or no more fresh oranges reachable
    """
    from collections import deque

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    # Find all initially rotten oranges (multi-source starting points)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))   # (row, col, minute)
            elif grid[r][c] == 1:
                fresh_count += 1

    if fresh_count == 0:
        return 0   # no fresh oranges to begin with

    max_minutes = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        r, c, minute = queue.popleft()
        max_minutes = max(max_minutes, minute)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == 1):
                grid[nr][nc] = 2          # rot it
                fresh_count -= 1
                queue.append((nr, nc, minute + 1))

    # If fresh oranges remain unreached, it's impossible
    return max_minutes if fresh_count == 0 else -1


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    grid1 = [[2,1,1],[1,1,0],[0,1,1]]
    assert oranges_rotting([row[:] for row in grid1]) == 4

    grid2 = [[2,1,1],[0,1,1],[1,0,1]]
    assert oranges_rotting([row[:] for row in grid2]) == -1

    grid3 = [[0,2]]
    assert oranges_rotting([row[:] for row in grid3]) == 0

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Multi-source BFS:
- Time:  O(m*n) — each cell visited at most once
- Space: O(m*n) — queue can hold all cells

KEY PATTERN LEARNED:
Multi-source BFS starts from ALL sources at once (all rotten
oranges), not sequentially. This models "simultaneous spreading"
correctly and is much simpler than trying to track time separately
for each source. This pattern extends to: Walls and Gates,
01 Matrix (distance to nearest 0).
"""
