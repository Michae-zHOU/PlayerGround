import heapq


class PriorityQueue:
    def __init__(self):
        self.heap = list()

    def __len__(self):
        return len(self.heap)

    def __iter__(self):
        return self.heap.__iter__()

    def push(self, element):
        heapq.heappush(self.heap, element)

    def pop(self):
        try:
            return heapq.heappop(self.heap)
        except Exception:
            raise Exception

    def clean(self):
        self.heap.clear()
