class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        validador = {}
        left = 0
        max_length = 0
        for right, char in enumerate(s):
            if char in validador and validador[char] >= left:
                left = validador[char] + 1
            validador[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length
        
