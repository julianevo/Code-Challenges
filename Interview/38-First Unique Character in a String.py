# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

    def firstUniqChar(s):
        if not s:
            return -1
        if len(s) == 1:
            return 0

        for i, ch in enumerate(s):
            if ch not in s[:i] + s[i+1]:
                return i 
        return -1

    def firstUniqChar(s):
        if not s:
            return -1
        if len(s) == 1:
            return 0
        
        index = len(s)
        for i in set(s):
            if s.count(i) == 1:
                index = min(index, s.index(i))
        return index if index != len(s) else -1