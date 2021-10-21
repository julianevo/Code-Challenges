# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

def moveZeroes (nums):
    l,r = 0,0
    while r < len(nums):
        if nums[l] == 0:
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            else:
                r += 1
        else:
            l += 1
            r += 1