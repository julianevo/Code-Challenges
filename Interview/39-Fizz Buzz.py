Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.


def FizzBuzz (n):
    res = []
    for x in range(1, n + 1):
        temp = ''
        if x % 3 == 0:
            temp += 'Fizz'
        if x % 5 == 0:
            temp += 'Buzz'
        if temp == '':
            temp += f'{x}'
        res.append(temp)
    return res