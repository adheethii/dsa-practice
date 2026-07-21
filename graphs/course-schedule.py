"""
Problem: Course Schedule
Difficulty: Medium
Category: Graphs / Topological Sort
LeetCode: #207

Problem Statement:
There are numCourses courses labeled 0 to numCourses-1. Given
prerequisites where prerequisites[i] = [a,b] means you must
take course b before course a, return true if you can finish
all courses (i.e., no cycle exists).

Example:
Input:  numCourses = 2, prerequisites = [[1,0]]
Output: True  (take 0 then 1)

Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: False  (0 needs 1, 1 needs 0 — cycle, impossible)
"""

# ─────────────────────────────────────────────
# APPROACH: DFS Cycle Detection
# Time: O(V + E) | Space: O(V + E)
# ─────────────────────────────────────────────

def can_finish(num_courses, prerequisites):
    """
    Key insight:
    This is a cycle detection problem on a directed graph.
    If there's a cycle in the prerequisite graph, it's
    impossible to complete all courses.

    Use DFS with THREE states per node:
    0 = unvisited
    1 = visiting (currently in the current DFS path)
    2 = visited (fully processed, no cycle through here)

    If we reach a node marked "visiting" (state 1) during DFS,
    we've found a cycle — course depends on itself indirectly.
    """
    # Build adjacency list: course -> list of prerequisites
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    state = [0] * num_courses   # 0=unvisited, 1=visiting, 2=visited

    def has_cycle(course):
        if state[course] == 1:
            return True    # found a cycle!
        if state[course] == 2:
            return False   # already fully processed, safe

        state[course] = 1   # mark as "visiting"

        for prereq in graph[course]:
            if has_cycle(prereq):
                return True

        state[course] = 2   # mark as fully "visited"
        return False

    for course in range(num_courses):
        if has_cycle(course):
            return False   # cycle found — impossible to finish

    return True   # no cycles — all courses can be completed


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert can_finish(2, [[1,0]]) == True
    assert can_finish(2, [[1,0],[0,1]]) == False
    assert can_finish(4, [[1,0],[2,0],[3,1],[3,2]]) == True
    assert can_finish(1, []) == True

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
DFS Cycle Detection:
- Time:  O(V + E) — visit every course and every prerequisite edge once
- Space: O(V + E) — adjacency list + recursion stack

KEY PATTERN LEARNED:
"Can all tasks be completed given dependencies" = cycle detection
in a directed graph. The 3-state trick (unvisited/visiting/visited)
is essential — a simple visited/unvisited boolean isn't enough to
detect cycles correctly in DIRECTED graphs. This exact pattern is
called Topological Sort / Course Schedule and appears frequently
in scheduling and dependency-resolution interview questions.
"""
