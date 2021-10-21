# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber1(nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key

def singleNumber2(nums):
    res = 0
    for num in nums:
        res ^= num
    return res
    
def singleNumber3(nums):
    return 2*sum(set(nums))-sum(nums)
    
def singleNumber4(nums):
    return reduce(lambda x, y: x ^ y, nums)
    
def singleNumber(nums):
    return reduce(operator.xor, nums)