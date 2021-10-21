You are given a string s. Consider the following algorithm applied to this string:

Take all the prefixes of the string, and choose the longest palindrome between them.
If this chosen prefix contains at least two characters, cut this prefix from s and go back to the first step with the updated string. Otherwise, end the algorithm with the current string s as a result.
Your task is to implement the above algorithm and return its result when applied to string s.
Note: you can click on the prefixes and palindrome words to see the definition of the terms if you're not familiar with them.

def checkPalindrome (prefix):
    prefArr = [c.lower() for c in prefix if c.isalum()]
    return prefArr == prefArr[::-1]

def palindromeCutting (s):
    arr1 = []
    arr2 = []
    i = 0
    j = 1

    while j <= len(s):
        arr1.append(s[i:j])
        j += 1
    arr1.sort(key == len)

    for item in arr1:
        if checkPalindrome(item) == True and len(item) >= 2:
            arr2.append(item)
    if len(arr2) == 0:
        return s
    else:
        var = s.strip(arr2[-1])
        if var != None:
            palindromeCutting(var)
    return ''

Example
For s = "aaacodedoc", the output should be palindromeCutting(s) = "".
The initial string s = "aaacodedoc" contains only three prefixes which are also palindromes - "a", "aa", "aaa". The longest one between them is "aaa", so we cut if from s.
Now we have string "codedoc". It contains two prefixes which are also palindromes - "c" and "codedoc". The longest one between them is "codedoc", so we cut if from the current string and obtain the empty string.
Finally the algorithm ends on the empty string, so the answer is "".
For s = "codesignal", the output should be palindromeCutting(s) = "codesignal".
The initial string s = "codesignal" contains the only prefix, which is also palindrome - "c". This prefix is the longest, but doesn't contain two characters, so the algorithm ends with string "codesignal" as a result.
For s = "", the output should be palindromeCutting(s) = "".
