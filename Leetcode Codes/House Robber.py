"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
can rob tonight without alerting the police.
"""
from typing import List
from collections import defaultdict


def rob(nums: List[int]) -> int:
    """
    >>> rob([6,3,6,7])
    13
    """
    dp = defaultdict(int)
    for i in range(len(nums), 0, -1):
        dp[i] = max(nums[i - 1] + dp[i + 2], dp[i + 1])
    return dp[1]

