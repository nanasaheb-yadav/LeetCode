"""
Problem:
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        >>> o = Solution()
        >>> o.searchInsert([1,3,5,6], 5)
        2
        >>> o.searchInsert([1,3,5,6], 2)
        1
        >>> o.searchInsert([1,3,5,6], 7)
        4
        >>> o.searchInsert([1,3,5,6], 0)
        0
        '''


        if target in nums:
            return nums.index(target)
        else:
            loc = 0
            for i in range(len(nums)):
                if nums[i] > target:
                    loc = i
                    break
                loc = i+1

            return loc


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #o = Solution()
    #val= o.searchInsert([1,3,5,6], 7)
    #print(val)


""":OUTPUT:

PS D:\> python -m doctest -v "35 Search Insert Position.py"
Trying:
    o = Solution()
Expecting nothing
ok
Trying:
    o.searchInsert([1,3,5,6], 5)
Expecting:
    2
ok
Trying:
    o.searchInsert([1,3,5,6], 2)
Expecting:
    1
ok
Trying:
    o.searchInsert([1,3,5,6], 7)
Expecting:
    4
ok
Trying:
    o.searchInsert([1,3,5,6], 0)
Expecting:
    0
ok
2 items had no tests:
    35 Search Insert Position
    35 Search Insert Position.Solution
1 items passed all tests:
   5 tests in 35 Search Insert Position.Solution.searchInsert
5 tests in 3 items.
5 passed and 0 failed.
Test passed.

"""