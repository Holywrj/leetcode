"""
给定一个只包含字符：
'(', ')', '{', '}', '[', ']'
的字符串 s，请判断字符串是否有效。

有效字符串需满足：
1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型左括号。
"""

class Solution:
    def is_valid_parentheses(self, strings: str) -> bool:
        stack = []
        match_dict = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        for s in strings:
            if s in ['}', ')', ']']:
                if not stack:
                    return False
                top = stack.pop()
                if top != match_dict.get(s):
                    return False
            else:
                stack.append(s)
        return not stack
