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
        >>> searchInsert(self,[1,3,5,6], 5)
        2
        >>> searchInsert(self, [1,3,5,6], 2)
        1
        >>> searchInsert(self, [1,3,5,6], 7)
        4
        >>> searchInsert(self, [1,3,5,6], 0)
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