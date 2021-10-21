# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

def isValid (s):
    x = len(s)
    if x == 0:
        return True
    
    if x % 2 != 0:
        return False
    
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('{}', '').replace('()', '').replace('[]', '')

    if s == ''
        return True
    else:
        return False

# Stack method

def isValid2 (s):
    stack = []
    dic = {']':'[', '}':'{', ')':'('}
    for i in s:
        if i in dic.values():
            stack.append(i)
        elif i in dic.keys():
            if stack == [] or dic[i] != stack.pop():
                return False
        else:
            return False
        return stack == []