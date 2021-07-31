"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i^th customer has in the jth bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.


Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.

"""

class Solution:
	
	def maximumWealth(self, accounts: List[List[int]]) -> int:
	
	# Solution 1: return max([sum(i) for i in accounts])
		"""
		sums every index in the list(list) and then uses max to grab the highest
		List comprehension BAY BEEEEE
		"""

	# Solution 2: return max(map(sum, accounts))
		"""
		returns the maximum of the map that sumds every item in accounts. this one is wild
		"""
	# Solution 3:
	
	maximumWealth = 0
	# Iterate through to perform actions at every index val
	for i in range(len(accounts)):
		# totalwealth
		totalWealth = sum(accounts[i])

		maxWealth = max(maxWealth, totalWealth)

	return maxWealth
