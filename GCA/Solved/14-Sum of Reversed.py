
Codewriting

Let's define the reverse of an integer x as the number obtained by reversing the order of the digits of x and then moving any leading zeroes to the end of the resulting number.

Expand to see the example video.

Given an array of integers arr, your task is to calculate the sum of reverse numbers of the elements of arr.

For arr = [7, 234, 58100], the output should be sumOfReversed(arr) = 18939.

The reverse of 7 is 7.
The reverse of 234 is 432.
The reverse of 58100 is 18500.
So the answer is 7 + 432 + 18500 = 18939.

	# check for leading 0 and append to the end
	# don't try to reverse 0, this will create an infinite loop

def sumOfReversed(arr):
    res = 0
    for i in arr:
        num = reverse(i)
        res += num
    return res
    
def reverse(i):
    revString = str(i)[::-1]
    if len(revString) > 1:
        while revString[0] == '0':
            revString = revString[1:] + '0'
    return int(revString)