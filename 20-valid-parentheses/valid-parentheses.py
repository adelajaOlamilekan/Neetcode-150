class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        brackets = deque()
        open_brackets = { "(", "{", "["}
        close_brackets = { ")", "}", "]" }
        bracket_map = { ")":"(", "}":"{", "]":"["}

        for char in s:
            if char in open_brackets:
                brackets.append(char)
            elif char in close_brackets and not brackets:
                return False
            elif char in close_brackets and brackets.pop() != bracket_map.get(char):
                return False
        
        if brackets:
            return False
        else:
            return True

        