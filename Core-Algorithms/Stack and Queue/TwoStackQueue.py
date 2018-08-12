class TwoStackQueue:
    def __init__(self):      
        self.stack = []
        self.buff = []
        return
    
    def __repr__(self):
        return "TwoStackQueue({0},{1})".format(self.stack, self.buff)
        
    def push(self, node):
        self.stack.append(node)
        return
        
    def pop(self):
        try:
            if len(self.buff) == 0:
                if len(self.stack) == 1:
                    return self.stack.pop()
                else:
                    while len(self.stack) > 0:
                        self.buff.append(self.stack.pop())
            return self.buff.pop()
        except IndexError:
            raise IndexError("pop from empty queue")
            return
