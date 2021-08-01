"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""

class Solution:
	def maxNumberOfBalloons(self, text: str) -> int:
		# My initial solution... not the best
		"""
		# So each character in the string can only be used once?
        # Can I assume that they are all one case? Upper or lower?
        # Can I assume that I will have a valid string to construct balloon with?
        
        valid = ['b','a','l','o','n']
        validString = "balloon"
        ans = 0 
        
        # for every element in the string
        for x in text:
            if x not in valid:
                text.strip()
            elif x in valid:
                current = x
                
        for _ in current:
            if _ == "b":
              
		"""

		# Better solution!
		
		# Use a dict with the letter for k, count for v
		counter = {"b":0, "a":0, "l":0, "o":0, "n":0}

		# Iterate through the str
		for char in text:
		
		    # Conditional to see if the char is in the dict
		    if char in counter:
			
			# Increment based on the return
			counter[char] += 1
		counter["l"] //= 2
		counter["o"] //= 2
		return min(counter.values())
