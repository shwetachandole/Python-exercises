'''
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

def two_sum(nums, target):
    comps = dict()
    for i, e in enumerate(nums):
        comp = target - e
        if comp in comps:
            return [comps[comp], i]
        comps[e] = i
    return[]


nums1 = [2,7,11,15]
target1 = 9
nums2 = [3,2,4]
target2 = 6
nums3 = [3,3]
target3 = 6
nums4 = [3,2,3]
target4 = 6

output1 = two_sum(nums1, target1)
print(output1)
output2 = two_sum(nums2, target2)
print(output2)
output3 = two_sum(nums3, target3)
print(output3)
output4 = two_sum(nums4, target4)
print(output4)
