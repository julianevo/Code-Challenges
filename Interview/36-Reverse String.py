Mirror Image Method

def reverseString (s):

    for i in range(len(s) // 2):
        s[i], s[-i-1] = s[-i-1], s[i]

Two Pointer Method

def reverseString (s):
    left,right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]

        left,right = left + 1, right - 1
