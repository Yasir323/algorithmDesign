# 4 operations: push, pop, peek or top, isEmpty
class MaxSizeError(Exception):
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


class Stack:
    
    def __init__(self, elements=None, maxlen=None):
        if elements is None:
            elements = []
        self._maxlen = maxlen
        if self._maxlen:
            if len(elements) > self._maxlen:
                raise MaxSizeError
        self.elements = elements

    def push(self, data):
        if not self._maxlen:
            self.elements.append(data)
        else:
            if len(self.elements) < self._maxlen:
                self.elements.append(data)
            else:
                raise MaxSizeError

    def pop(self):
        if self.elements:
            return self.elements.pop()
        else:
            raise EmptyStackError
    
    def __len__(self):
        return len(self.elements)

    def is_empty(self):
        return True if len(self.elements) == 0 else False
    
    def peek(self):
        return self.elements[-1]
    
    def __repr__(self) -> str:
        return f"{self.elements}"
    
    def __str__(self) -> str:
        return f"{self.elements}"


if __name__ == '__main__':
    stack = Stack([1, 2, 3], maxlen=5)
    print(f"Original stack: {stack}")
    stack.push(4)
    print(f"After pushing 4: {stack}")
    stack.pop()
    print(f"After popping: {stack}")
    print(f"Length of stack: {len(stack)}")
    print(f"Top of the stack: {stack.peek()}")
    print(f"Is the stack empty: {stack.is_empty()}")
