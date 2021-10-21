# Return true if integer is a palindrome 
#Palindrome is an integer read backward same as forward (121 = 121, 123 != 321)

def palindrome (x):
    
    str_list = list(str(x))
    str_list2 = str_list[::-1]

    if (str_list == str_list2):
        return True
    else:
        return False



