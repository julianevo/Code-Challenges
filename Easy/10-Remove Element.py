# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
# Return k after placing the final result in the first k slots of nums.

Starting from the left every time we find a value that is the target value we swap it out with an item starting from the right. We decrement end each time as we know that the final item is the target value and only increment start once we know the value is ok. Once start reaches end we know all items after that point are the target value so we can stop there.


def removeElement (nums,val):
    start, end = 0, len(nums) - 1
    while start <= end:
        if nums[start] == val:
            nums[start], nums[end], end = nums[end], nums[start], - 1
        else:
            start += 1
    return start

def removeElement2 (nums,val):
    count = 0
    for i in nums:
        if i != val:
            nums[count] = i
            count += 1
    return count