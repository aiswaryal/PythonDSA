"""You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.
Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.
Example 3:

Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i], target <= 100"""

class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        min = 0
        max = len(nums) - 1
        while min <= max:
            pos = (min + max) // 2
            if target == nums[pos]:
                first = last = pos
                # find first occurrence
                if first - 1 >= 0:
                    while first != 0 and nums[first] == nums[first-1]:
                        first -= 1
                    # find last occurrence
                if last != len(nums) - 1:
                     while last != len(nums) - 1 and nums[last] == nums[last+1]:
                        last += 1
                else:
                # only one 'target' was found
                     return [first]
                return list(range(first,last+1))

            elif target < nums[pos]:
                max = pos - 1
            else:
                min = pos + 1
