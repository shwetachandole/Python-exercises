# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
'''
Given an integer array nums and an integer k,
return the maximum length of a subarray that sums to k.
If there is not one, return 0 instead.

Example 1:
Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

Example 2:
Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
'''

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        cumulative_sum = 0
        max_len_subarray = 0
        indices = dict()

        for index, element in enumerate(nums):
            cumulative_sum += element

            if cumulative_sum == k:
                max_len_subarray = index + 1

            if (cumulative_sum - k) in indices:
                max_len_subarray = max(max_len_subarray, index - indices[cumulative_sum - k])

            if cumulative_sum not in indices:
                indices[cumulative_sum] = index

        return max_len_subarray
