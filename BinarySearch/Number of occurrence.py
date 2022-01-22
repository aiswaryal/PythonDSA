""" Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.

Example 1:

Input:
N = 7, X = 2
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 4
Explanation: 2 occurs 4 times in the
given array.
Example 2:

Input:
N = 7, X = 4
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 0
Explanation: 4 is not present in the
given array.
Your Task:
You don't need to read input or print anything. Your task is to complete the function count() which takes the array of integers arr, n and x as parameters and returns an integer denoting the answer.

Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
1 ≤ Arr[i] ≤ 106
1 ≤ X ≤ 106"""

class Solution:
    def searchNum(self, nums, x):
        
        low = 0
        high = len(nums) -1
        while low <=high:
            mid = low + (high-low)//2
            if nums[mid] == x:
                return mid
            elif nums[mid] > x:
                high = mid-1
            else:
                low = mid+1


    def count(self,arr, n, x):
        # code here
        nums = arr
        if not nums:
            return 0
        
        index = self.searchNum(nums, x)
        if index is None:
            return 0
        lowIndex = index
        while 0 <= lowIndex < len(nums) and nums[lowIndex] == x:
            lowIndex-= 1
        highIndex = index
        while 0 <= highIndex < len(nums) and nums[highIndex] == x:
            highIndex += 1
        return (highIndex- lowIndex -1)
