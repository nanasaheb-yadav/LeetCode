"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


def lengthOfLastWord(s: str) -> int:

    """
    >>> lengthOfLastWord("Hello World")
    5
    >>> lengthOfLastWord("   fly me   to   the moon  ")
    4
    >>> lengthOfLastWord("luffy is still joyboy")
    6
    >>> lengthOfLastWord("Hi")
    2
    """
    return len(s.split()[-1])


"""OUTPUT:
PS D:Leetcode Codes> python -m doctest -v '.\Length of Last Word.py'
Trying:
    lengthOfLastWord("Hello World")
Expecting:
    5
ok
Trying:
    lengthOfLastWord("   fly me   to   the moon  ")
Expecting:
    4
ok
Trying:
    lengthOfLastWord("luffy is still joyboy")
Expecting:
    6
ok
Trying:
    lengthOfLastWord("Hi")
Expecting:
    2
ok
1 items had no tests:
    Length of Last Word
1 items passed all tests:
   4 tests in Length of Last Word.lengthOfLastWord
4 tests in 2 items.
4 passed and 0 failed.
Test passed.

"""