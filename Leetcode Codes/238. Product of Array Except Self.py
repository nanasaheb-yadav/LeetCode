"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    prod = []
    n = len(nums)
    if n == 1:
        return [0]
    else:
        """for i in range(0, n):
            a1 = nums[:i]
            a2 = nums[i + 1:]
            a1.extend(a2)
            result = 1
            for j in range(0, len(a1)):
                result = result * a1[j]
            prod.append(result)
        return prod"""
        left = [1] * len(nums)

        right = [1] * len(nums)
        count = 1

        for i in range(len(nums)):
            left[i] = count
            count *= nums[i]

        count = 1
        for i in range(len(nums) - 1, -1, -1):
            right[i] = count
            count *= nums[i]
        for i in range(len(nums)):
            left[i] *= right[i]

        return left


# Driver Code
ar = [1, 2, 3, 4, 5]

print(productExceptSelf(ar))
