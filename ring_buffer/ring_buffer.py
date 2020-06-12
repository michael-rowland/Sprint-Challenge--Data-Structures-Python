class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.data = []

    def append(self, item):
        if self.current < self.capacity:
            self.data.append(item)
        else:
            self.data[self.current % self.capacity] = item
        self.current += 1

    def get(self):
        return self.data