class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        parts = []
        i = j = 0
        while i < len(word1) and j < len(word2):
            parts.append(word1[i])
            parts.append(word2[j])
            i += 1
            j += 1
        parts.append(word1[i:])
        parts.append(word2[j:])
        return "".join(parts)
