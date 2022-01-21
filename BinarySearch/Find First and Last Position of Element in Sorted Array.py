"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
 
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
 
Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

class Solution:
    def searchNum(self, nums, target):
        
        low = 0
        high = len(nums) -1
        while low <=high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        
        index = self.searchNum(nums, target)
        if index is None:
            return [-1, -1]
        lowIndex = index
        while 0 <= lowIndex < len(nums) and nums[lowIndex] == target:
            lowIndex-= 1
        highIndex = index
        while 0 <= highIndex < len(nums) and nums[highIndex] == target:
            highIndex += 1
        return [lowIndex+1, highIndex-1]
