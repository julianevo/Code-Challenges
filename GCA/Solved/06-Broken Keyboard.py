For text = "Hello, this is CodeSignal!" and letters = ['e', 'i', 'h', 'l', 'o', 's'],
the output should be brokenKeyboard(text, letters) = 2.

For text = "Hi, this is Chris!" and letters = ['r', 's', 't', 'c', 'h'], the output should be
brokenKeyboard(text, letters) = 0.

For text = "3 + 2 = 5" and letters = [], the output should be brokenKeyboard(text, letters) = 5.

def brokenKeyboard (text,letters):
    words = text.split()
    letters = set(letters)
    ans = 0
    flag = True
    for word in words:
        flag = True
        for letter in word:
            if ('a' <= letter <= 'z' or 'A' <= letter <= 'Z') and letter.lower() not in letters:
                flag = False
                break 
        if flag:
            ans += 1
        
    return ans
