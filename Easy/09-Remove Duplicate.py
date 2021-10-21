# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

def removeDup (a):
    if not a:
        return 0
    
    new = 0

    for i in range (1, len(a)):
        if a[i] != a[new]:
            new += 1
            a[new] = a[i]

    return new + 1
