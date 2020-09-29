class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest_index = 0
        self.data = []
 
    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else: 
            self.data[self.oldest_index] = item
            if self.oldest_index < len(self.data) - 1:
                self.oldest_index += 1
            else:
                self.oldest_index = 0
    
    def get(self):
        return [item for item in self.data if item]