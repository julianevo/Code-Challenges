# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

class minStack:
    def __init__ (self):
        # initialize data structure here 
        self.x = []
    
    def push (self, i):
        self.x.append(i)

    def pop (self):
        self.x.pop()

    def top (self):
        # fetch latest element from stack
        return self.x[-1]

    def getMin (self):
        return min(self.x)