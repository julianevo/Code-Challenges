# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

def mySqrt (x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    low = 0
    high = x
    
    while low < high:
        mid = low + (high-low) // 2
        if mid ** 2 <= x:
            low = mid + 1
        else:
            high = mid
    return low - 1