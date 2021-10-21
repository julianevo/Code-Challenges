You've created a new programming language, and now you've decided to add hashmap support to it. Actually you are quite disappointed that in common programming languages it's impossible to add a number to all hashmap keys, or all its values. So you've decided to take matters into your own hands and implement your own hashmap in your new language that has the following operations:

1) insert x y - insert an object with key x and value y.

2) get x - return the value of an object with key x.

3) addToKey x - add x to all keys in map.

4) addToValue y - add y to all values in map.

5) To test out your new hashmap, you have a list of queries in the form of two arrays: queryTypes contains the names of the methods to be called (eg: insert, get, etc), and queries contains the arguments for those methods (the x and y values).

Your task is to implement this hashmap, apply the given queries, and to find the sum of all the results for get operations.


def hashMap (queryType, query):
    d = {}
    x = 0
    keys = 0
    values = 0

    for i,j in zip(queryType,query):

        if i == 'insert':
            d[j[0]-keys] = j[1] - values

        elif i == 'addToValue':
            values += j[0]
            
        elif i == 'addToKey':
            keys += j[0]

        elif i == 'get':
            x += d[j[0]-keys] + values

    return x




Example
For queryType = ["insert", "addToValue", "addToKey", "get"] and query = [[1, 2], [2, 3], [2], [1], [3]], the output should be hashMap(queryType, query) = 5.
The hashmap looks like this after each query:
1 query: {1: 2}
2 query: {1: 2, 2: 3}
3 query: {1: 4, 2: 5}
4 query: {2: 4, 3: 5}
5 query: answer is 5
The result of the last get query for 3 is 5 in the resulting hashmap.
For queryType = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"] and query = [[1, 2], [2], [1], [2, 3], [1], [-1], [3]], the output should be hashMap(queryType, query) = 6.
The hashmap looks like this after each query:
1 query: {1: 2}
2 query: {1: 4}
3 query: answer is 4
4 query: {1: 4, 2: 3}
5 query: {2: 4, 3: 3}
6 query: {2: 3, 3: 2}
7 query: answer is 2
The sum of the results for all the get queries is equal to 4 + 2 = 6.