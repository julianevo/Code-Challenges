# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSum (nums, target):
	i=0
	while i < len(nums):
		required = target - nums(i)
		try:
			second = nums.index(required, i + 1)
			break
		except ValueError:
			i += 1
	return (i, second)