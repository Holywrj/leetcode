"""
l1 = [2,4,3]
l2 = [5,6,4]
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            total = num1 + num2 + carry

            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


if __name__ == "__main__":
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print(linked_list_to_list(result))
