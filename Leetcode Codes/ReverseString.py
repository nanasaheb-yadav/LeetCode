from typing import List


def reverseString(s: List[str]):
    """
    Do not return anything, modify s in-place instead.
    """
    s = s[::-1]
    return s

print(reverseString(["h","e","l","l","o"]))