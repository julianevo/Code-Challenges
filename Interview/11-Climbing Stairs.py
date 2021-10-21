# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Fibonacci Sequence

def climbStairs (n):
    a,b = 1,1
    for i in range(n):
        a,b = b, a+b
    return a 

Constant space

def climbStairs2 (n):
    if n == 1:
        return 1
    a,b = 1,2
    for i in xrange(2, n)
        tmp = b
        b = a+b
        a = tmp
    return b