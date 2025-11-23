class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)

        # If minStack is empty or the new value is <= current min, push it
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        else:
            # Repeat the current minimum for constant-time getMin
            self.minStack.append(self.minStack[-1])

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]
