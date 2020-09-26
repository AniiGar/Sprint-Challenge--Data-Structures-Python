class RingBuffer:
    def __init__(self, capacity):
        self.max = capacity
        self.cur = None
        self.data = []

    class Full:
        def append(self, item):
            self.data[self.cur] = item
            self.cur = (self.cur+1) % self.max
        
        def get(self):
            return self.data[self.cur:] + self.data[:self.cur]

    def append(self, item):
        self.data.append(item)
        if len(self.data) == self.max:
            self.cur = 0
            self._class_ = self.Full

    def get(self):
        return self.data