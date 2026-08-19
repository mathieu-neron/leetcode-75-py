# LeetCode 2462: Total Cost to Hire K Workers
# https://leetcode.com/problems/total-cost-to-hire-k-workers/

import heapq

class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        left, right = [], []
        lo, hi = 0, n - 1

        for _ in range(candidates):
            if lo <= hi:
                heapq.heappush(left, costs[lo]);
                lo += 1
            if lo <= hi:
                heapq.heappush(right, costs[hi]);
                hi -= 1

        total = 0
        for _ in range(k):
            if right and (not left or right[0] < left[0]):
                total += heapq.heappop(right)
                if lo <= hi:
                    heapq.heappush(right, costs[hi]);
                    hi -= 1
            else:
                total += heapq.heappop(left)
                if lo <= hi:
                    heapq.heappush(left, costs[lo]);
                    lo += 1

        return total
