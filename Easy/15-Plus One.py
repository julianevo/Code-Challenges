# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

def plusOne (digits):
    num = 0
    for i in range(len(digits)):
        num += digits[i] * pow(10, (len(digits) - 1 - i))
    return [int(i) for i in str(num + 1)]


We're given a list of digits, and the idea here is to convert that list to an integer, num. So each digit is multiplied by the proper place value and added to num. For example, if digits = [3, 8, 2, 5] then on the first iteration 3 is multiplied by 10 to the power of 4-1-0 = 3, so this results in 3000, which is added to num. Then 8 is multiplied by 10^2 and added to num, and so on.

The last step is to add 1 to num, convert it to a list and return that list.