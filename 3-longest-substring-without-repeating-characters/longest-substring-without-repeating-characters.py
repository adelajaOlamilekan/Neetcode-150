class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque

        substring = deque([])
        max_length = 0
        for char in s:
            while char in substring:
                max_length = max(max_length, len(substring))
                substring.popleft()
            substring.append(char)
            max_length = max(max_length, len(substring))
        
        return max_length




        