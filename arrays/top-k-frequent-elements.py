"""
Problem: Top K Frequent Elements
Difficulty: Medium
Category: Arrays / Heap
LeetCode: #347

Problem Statement:
Given an integer array nums and an integer k, return the k
most frequent elements. You may return the answer in any order.

Example:
Input:  nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

# ─────────────────────────────────────────────
# APPROACH 1: Sort by Frequency
# Time: O(n log n) | Space: O(n)
# ─────────────────────────────────────────────

def top_k_frequent_sort(nums, k):
    from collections import Counter
    count = Counter(nums)
    sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_items[:k]]


# ─────────────────────────────────────────────
# APPROACH 2: Heap (Optimal for large n, small k)
# Time: O(n log k) | Space: O(n)
# ─────────────────────────────────────────────

def top_k_frequent(nums, k):
    """
    Key insight:
    Use a min-heap of size k. For each unique number,
    push (frequency, number). If heap exceeds size k,
    pop the smallest — this keeps only the k LARGEST
    frequencies in the heap at all times.

    Example walkthrough:
    nums = [1,1,1,2,2,3], k=2
    Frequencies: {1:3, 2:2, 3:1}

    Push (3,1) → heap=[(3,1)]
    Push (2,2) → heap=[(2,2),(3,1)]
    Push (1,3) → heap size > 2 → pop smallest (1,3)
                 → heap=[(2,2),(3,1)]

    Result: [1, 2] (extract numbers from heap) ✅
    """
    import heapq
    from collections import Counter

    count = Counter(nums)
    heap = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)   # remove smallest frequency

    return [num for freq, num in heap]


# ─────────────────────────────────────────────
# APPROACH 3: Bucket Sort (Optimal — O(n))
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────

def top_k_frequent_bucket(nums, k):
    from collections import Counter

    count = Counter(nums)
    # buckets[i] = list of numbers that appear exactly i times
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result

    return result


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert set(top_k_frequent([1,1,1,2,2,3], 2)) == {1, 2}
    assert set(top_k_frequent([1], 1)) == {1}
    assert set(top_k_frequent_bucket([1,1,1,2,2,3], 2)) == {1, 2}

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Heap Approach:
- Time:  O(n log k) — better than O(n log n) when k is small
- Space: O(n) — for the frequency counter

Bucket Sort (Optimal):
- Time:  O(n) — no sorting needed, indices ARE the frequency
- Space: O(n)

KEY PATTERN LEARNED:
"Top K" problems → think Heap (keep only k best seen so far)
or Bucket Sort (when frequency range is bounded by array length).
Min-heap of size k is a classic trick for "top K largest" —
counterintuitively you POP the smallest to keep the largest k.
"""
