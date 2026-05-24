# LeetCode 1431: Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        n = len(candies)
        max = max(candies)
        result = []

        for i in range(n):
            if candies[i] + extraCandies >= max:
                result.append(True)
            else:
                result.append(False)
        return result
