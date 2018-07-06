class MyStack:
    # implement stack by three queues
    def __init__(self):
        """
        Initialize your data structure here.
        """
        import queue
        self.queue0 = queue.Queue()
        self.queue1 = queue.Queue()
        self.buffer = queue.Queue()
        self.indicator = 0         

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.indicator == 0:
            self.queue0.put_nowait(x)
            self.indicator = 1
        else:
            self.queue1.put_nowait(x)
            self.indicator = 0

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            raise IndexError("pop from empty stack")
            return
        if self.indicator == 0:
            while True:
                tmp = self.queue1.get_nowait()
                if self.queue1.empty():
                    self.buffer, self.queue1 = self.queue1, self.buffer
                    self.indicator = 1
                    return tmp
                else:
                    self.buffer.put_nowait(tmp)
            
        else:
            while True:
                tmp = self.queue0.get_nowait()
                if self.queue0.empty():
                    self.buffer, self.queue0 = self.queue0, self.buffer
                    self.indicator = 0
                    return tmp
                else:
                    self.buffer.put_nowait(tmp)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            raise IndexError("stack index out of range")
            return
        if self.indicator == 0:
            while True:
                tmp = self.queue1.get_nowait()
                self.buffer.put_nowait(tmp)
                if self.queue1.empty():
                    self.buffer, self.queue1 = self.queue1, self.buffer
                    return tmp
        else:
            while True:
                tmp = self.queue0.get_nowait()
                self.buffer.put_nowait(tmp)
                if self.queue0.empty():
                    self.buffer, self.queue0 = self.queue0, self.buffer
                    return tmp

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue0.empty() and self.queue1.empty()
