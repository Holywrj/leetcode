"""
给定一个整数数组 nums 和一个整数 target，
请你在数组中找出和为 target 的那两个整数，
并返回它们的下标。

你可以假设每种输入只会对应一个答案，
但是，同一个元素不能使用两遍。

可以按任意顺序返回答案。
nums = [2, 7, 11, 15]
target = 9
[0, 1]
"""

"""
一边遍历数组，一边用 HashMap 记录已经见过的数字及其下标。
对当前数字 num，只需要检查 target - num 是否已经出现
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
