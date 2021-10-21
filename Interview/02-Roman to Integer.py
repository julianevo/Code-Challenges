# Roman to numbers
# (I = 1) (V = 5) (X = 10) (L = 50) (C = 100) (D = 500) (M = 1000)

def romanToInt (s):
    # key value = roman, decimal
    table = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    } 
    # integer value
    number = 0

    # scan each integer value
    for i, char in enumerate(s):
        # add value
        number += table[char]

        if i and (table[char] > table[s[i-1]]):
            # adjustment for IV,IX,XL,XC,CD,CM
            number -= 2 * table [s[i-1]]
    return number