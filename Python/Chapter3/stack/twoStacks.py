"""
Create a data structure twoStacks that represents two stacks. 
Implementation of twoStacks should use only one array, i.e., 
both stacks should use the same array for storing elements.

The idea is to start two stacks from two extreme corners of 
arr[]. stack1 starts from the leftmost element, the first 
element in stack1 is pushed at index 0. The stack2 starts from 
the rightmost corner, the first element in stack2 is pushed at 
index (n-1). Both stacks grow (or shrink) in opposite direction. 
To check for overflow, all we need to check is for space between 
top elements of both stacks.
"""

from array import array

MAX = 32768


class StackOverflowError(Exception):
    """Raised when stack is full."""

    def __init__(self, message="Stack is full") -> None:
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return self.message


class EmptyStackError(Exception):
    """Raised when stack is empty."""

    def __init__(self, message="Stack is empty") -> None:
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return self.message


class TwoStacks:

    def __init__(self, n):
        self.size = n
        self.arr = array('i', [MAX] * n)
        self.top1 = -1
        self.top2 = self.size

    def push1(self, x):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x
        else:
            raise StackOverflowError

    def push2(self, x):
        if self.top2 > self.top1 + 1:
            self.top2 -= 1
            self.arr[self.top2] = x
        else:
            raise StackOverflowError

    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.arr[self.top1] = MAX
            self.top1 -= 1
            return x
        else:
            raise EmptyStackError

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.arr[self.top2] = MAX
            self.top2 += 1
            return x
        else:
            raise EmptyStackError


# Driver program to test twoStacks class
ts = TwoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)
print("Popped element from stack1 is " + str(ts.pop1()))
ts.push2(40)
print("Popped element from stack2 is " + str(ts.pop2()))
ts.push2(400)
try:
    ts.push2(0)
except Exception as e:
    print(f"{type(e).__name__}: {str(e)}")
