# Reverse String

def rev (s):
	#one points to the head position and the other to the tail position
	left = 0
	right = len(s)-1
	#reverse string by two pointers 
	while left < right:
		s[left],s[right] = s[right], s[left]
		left += 1
		right -= 1
	return s