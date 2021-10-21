# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


# Sort the nums then a brute force will do the work, and don't forget that the index of the current element must be equal to the this element (exp: i = 0, nums[0] == 0) if not return i (exp : i = 2 nums[2] == 3 so missing number = i)


def missingNumber (nums):
    nums.sort()
    for i in range(len(nums)):
        if i != nums[i]:
            return i
    return len(nums)