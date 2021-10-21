# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Counter(s) == Counter(t) is accepted as a solution

def isAnagram (s,t):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in t:
        if i in d: 
            d[i] -= 1
        else:
            return False 
    for k,v in d.items():
        if v != 0:
            return False 
    return True