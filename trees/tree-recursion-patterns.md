# Recognizing Tree Recursion Patterns

**Date:** 2026-08-07

## Why This Note

After working through 15 tree problems now (Max Depth, Diameter,
LCA-BST, Same Tree, Invert, Subtree, Level Order, Right Side View,
Path Sum, Max Path Sum, Kth Smallest, Construct from Traversals,
Insert-BST, Delete-BST, Balanced), a genuinely useful exercise is
naming the HANDFUL of underlying shapes they all reduce to, rather
than treating each as a separate thing to memorize.

---

## Shape 1 — Bottom-Up Combine (the most common shape)

```
Recurse on left, recurse on right, COMBINE the two results at
the current node, return that combination upward.

def solve(node):
    if not node:
        return <base_case_value>
    left_result = solve(node.left)
    right_result = solve(node.right)
    return <combine left_result and right_result somehow>
```

Problems using this shape: Maximum Depth (`combine = 1 + max(l, r)`),
Diameter (combine = check `l + r` against a running max, THEN
return `1 + max(l, r)` upward — two things happening at once),
Balanced Binary Tree (combine = check `abs(l - r) > 1`, propagate
a -1 sentinel on failure).

---

## Shape 2 — Top-Down Pass-a-Value-Down

```
Instead of building an answer from the bottom up, pass CONTEXT
down from parent to child (a target sum remaining, a valid
value range, a running path) — the answer emerges when a base
case is hit deep in the tree, not by combining subtree results.

def solve(node, context):
    if not node:
        return <base case, often False or an empty result>
    if <node is a leaf and satisfies the goal given this context>:
        return True
    return solve(node.left, updated_context) or solve(node.right, updated_context)
```

Problems using this shape: Path Sum (context = remaining sum
needed), Validate BST from an earlier session (context = valid
(min, max) range), Insert into BST and Delete Node in BST (context
= which direction the target value implies, following BST order).

---

## Shape 3 — Level-by-Level BFS (not recursion at all)

```
Some tree problems are naturally about LEVELS, not paths — these
don't fit either recursive shape well and are cleaner as BFS with
an explicit queue, processing one full level before the next.

from collections import deque
def solve(root):
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            # process node — it's part of the CURRENT level
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
```

Problems using this shape: Level Order Traversal, Right Side View
(same BFS, just keep only the last node processed per level).

---

## The Recognition Question Worth Asking First

```
"Does the answer come from COMBINING what happened in both
 subtrees (Shape 1), or from CARRYING something down and
 checking it against a base case (Shape 2), or is this
 fundamentally about LEVELS rather than paths (Shape 3)?"
```

Diameter of Binary Tree is a genuinely instructive edge case here
— it looks like it should be Shape 2 (find the longest path) but
is actually solved with Shape 1 (bottom-up height combining, with
a side-effect check at each node) — a reminder that the SHAPE
that fits isn't always the one that first seems obvious from how
the problem is phrased.

---

## Key Takeaway

> Three recurring shapes cover nearly every tree problem worked through so far: bottom-up combine (build the answer from subtree results), top-down context-passing (carry information down, resolve at a base case), and level-order BFS (for genuinely level-based questions, not path-based ones). Asking "which of these three does this actually reduce to" before writing code is a more transferable skill than remembering each of the 15 individual solutions separately.
