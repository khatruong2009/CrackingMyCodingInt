"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""


class Solution:
	
	def defangIPAddr(self, address: str) -> str:
		# Uses the replace lib in Py3
		# The three indicates the max number of times to cover an edge case...
		return address.replace(".", "[.]", 3)
