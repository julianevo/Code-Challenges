# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longestCommonPrefix (strs):
    if not strs:
        return ''
    
    shortest = min(strs, key = len)

    for i, ch in enumerate(shortest):
        for extra in strs:
            if extra[i] != ch:
                return shortest[:i]
    return shortest

# Create one iterator per string using zip, it will stop at the shortest string
# s is a tuple of characters at current position for each string
# create a set to test unicity
def longestCommonPrefix2 (strs):
    result = []
    for i in zip(*strs):
        if len(set(i)) != 1:
            break
        result.append(i[0])
    return ''.join(result)