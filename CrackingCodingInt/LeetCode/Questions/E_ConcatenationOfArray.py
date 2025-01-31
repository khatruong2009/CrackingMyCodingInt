"""

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]

Explanation: The array ans is formed as follows:

- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

"""


class Solution:

	def getConcatenation(self, nums: List[int]) -> List[int]:
		"""		
 		For every item in the list, up until the last index in the original list,
		take the term and then duplicate it.
		"""
		
		# Solution 1 = return nums + nums (47ms)
		
		"""
		Solution 2
		
		nums.extend(nums)
		return nums
		"""
		return nums + nums
