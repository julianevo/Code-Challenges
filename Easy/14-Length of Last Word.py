# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.


def lengthOfLastWord(s):
    if s is None:
        return 0
    if s.strip() == '':
        return 0
    return (len(s.split()[-1]))

