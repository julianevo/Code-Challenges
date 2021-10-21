# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

def isHappy (n):
    if n == 1:
        return true
    l = []

    def calculate(n):
        c = 0
        for i in str(n):
            c += int(i) ** 2
        return c
    
    while n != 1:
        n = calculate(n)
        if n in l:
            return False
        l.append(n)
    return True