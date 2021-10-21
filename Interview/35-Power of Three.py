# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

Brute Force:

def isPowerOfThree (n):
    if n == 0:
        return 0
    while n % 3 == 0:
        n //= 3
    return True if n == 1 else False 

Recursion:

def isPowerOfThree (n):
    if n <= 0:
        return False 
    if n == 1:
        return True
    if n % 3 == 0:
        return self.isPowerOfThree(n//3)
    return False 

## take advantage of highest limitation is 3**19 = 1162261467 since Integer has range <2147483648, so if 1162261467 % n == 0, then True
    def isPowerOfThree(n):
        return n > 0 and 1162261467 % n == 0