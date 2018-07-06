class MyQueue:
    # implement queue by two stacks
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack0 = []
        self.stack1 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack0.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack1) > 0:
            return self.stack1.pop()
        elif len(self.stack0) > 0:
            n = len(self.stack0)
            for i in range(n-1):
                tmp = self.stack0.pop()
                self.stack1.append(tmp)
            return self.stack0.pop()
        else:
            raise IndexError('pop from empty queue !')
            return

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack1) > 0:
            return self.stack1[-1]
        elif len(self.stack0) > 0:
            n = len(self.stack0)
            for i in range(n):
                tmp = self.stack0.pop()
                self.stack1.append(tmp)
            return self.stack1[-1]
        else:
            raise IndexError("queue index out of range !")
            return

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack0) == 0 and len(self.stack1) == 0
