"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


def isValidParanthesis(s: str) -> bool:

    """
    >>> isValidParanthesis("()")
    True
    >>> isValidParanthesis("()[]{}")
    True
    >>> isValidParanthesis("()[]{")
    False
    >>> isValidParanthesis("(]")
    False
    """
    braces = ['()', '{}', '[]']

    while any(x in s for x in braces):
        for b in braces:
            s = s.replace(b, '')
    return not s


"""
OUTPUT:
PS D:\LeetCode\Leetcode Codes> python -m doctest -v 'Valid Parentheses.py'
Trying:
    isValidParanthesis("()")
Expecting:
    True
ok
Trying:
    isValidParanthesis("()[]{}")
Expecting:
    True
ok
Trying:
    isValidParanthesis("()[]{")
Expecting:
    False
ok
Trying:
    isValidParanthesis("(]")
Expecting:
    False
ok
1 items had no tests:
    Valid Parentheses
1 items passed all tests:
   4 tests in Valid Parentheses.isValidParanthesis
4 tests in 2 items.
4 passed and 0 failed.
Test passed.

"""