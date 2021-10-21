# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

def titleToNumber (s):
    res = 0
    val = [i for i in range(1,27)]
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    d = dict(zip(letters,val))
    for ch i in s:
        res = res * 26 + d[ch]
    return res