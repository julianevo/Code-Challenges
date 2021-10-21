# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containDuplicate (nums):
    nums = sorted(nums)

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True 
    return False 

    # METHOD 3: using sets
	# return len(nums) != len(set(nums))

        #  d=dict()
        # for i in (nums):
        #     if i in d:
        #         return True
        #     else:
        #         d[i]=1        
        # return False
        