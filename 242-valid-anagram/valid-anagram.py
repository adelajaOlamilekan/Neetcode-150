class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = dict()
        t_map = dict()

        if len(s) != len(t):
            return False

        for char in s:
            s_map[char] = s_map.get(char, 0) + 1
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1

        for key in s_map.keys():
            if t_map.get(key, 0) != s_map.get(key, 0):
                return False
        
        return True
