class minStack:
    def __init__(self):
        self.stack = []
        self.minHistory = []
        return
    
    def push(self, node):
        self.stack.append(node)
        if len(self.minHistory) == 0 or self.minHistory[-1] > node:
            self.minHistory.append(node)
        else:
            self.minHistory.append(self.minHistory[-1])
        return
        
    def pop(self):
        self.minHistory.pop()
        return self.stack.pop()
        
    def top(self):
        return self.stack[-1]
        
    def min(self):
        return self.minHistory[-1]
