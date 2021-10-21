Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

def hammingWeight (n):
    res = 0
    while n:
        res += n % 2
        n = n >> 1  # move binary number "right" once
    return res