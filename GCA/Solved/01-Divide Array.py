Given an array of integers a of even length, your task is to split it into two arrays of equal length such that all the numbers are unique in each of them.

There may be more than one possible answer, in which case you may return any of them. If there are no possible answers, return an empty array.

Hint: Count the number of occurrences of each integer in a. If there are integers occurring more than twice, then there is no solution. Next, put the integers occurring twice into both answer arrays. Finally, put all other numbers in the answer arrays, following the condition that they should have equal sizes.

For a = [2, 1, 2, 3, 3, 4], the output can be divideArray(a) = [[2, 1, 3], [2, 3, 4]].

Answers like [[1, 2, 3], [2, 3, 4]] or [[4, 2, 3], [3, 2, 1]] would also be considered correct.

For a = [1, 2, 2, 1], the output can be divideArray(a) = [[1, 2], [2, 1]].

Again, there are other possible answers.

For a = [2, 2, 3, 3, 2, 2], the output should be divideArray(a) = [].

No matter how we try to split this array, there will be at least two 2s in at least one of the resulting arrays. So the answer is [].

def divideArray (a):
