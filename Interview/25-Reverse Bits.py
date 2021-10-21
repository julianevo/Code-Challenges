# Reverse bits of a given 32 bits unsigned integer.

def reverseBits (n):
    res = 0
    for i in range(32): # 32 integer bit
        res = res << 1 # left shift to check it till 32 bits
        res += n % 2 # checking if rightmost bit of n is 1 and adding to result
        n = n >> 1 # checking all bits of n till n becomes 0
    return res
