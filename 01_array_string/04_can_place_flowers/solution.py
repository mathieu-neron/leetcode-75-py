# LeetCode 605: Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        f = len(flowerbed)
        i = 0

        while i<f:
            if flowerbed[i]==1:
                i = i + 2
            elif i == f-1 or flowerbed[i+1]==0:
                n = n - 1
                i = i+2
            else:
                i = i + 3
        return n <= 0
