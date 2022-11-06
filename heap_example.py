class Heap:
    def __init__(self, max_size=100):
        self.MAX_SIZE = max_size
        self.heap = [None] * self.MAX_SIZE
        self.size = 0

    @staticmethod
    def get_parent(index):
        return (index - 1) // 2

    @staticmethod
    def get_left_child(index):
        return 2 * index + 1

    @staticmethod
    def get_right_child(index):
        return 2 * index + 2

    def insert(self, element):
        if self.size == self.MAX_SIZE:
            return -1
        self.heap[self.size] = element
        self.sift_up(self.size)
        self.size += 1

    def extract_min(self):
        min_element = self.heap[0]
        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], None
        self.size -= 1
        self.sift_down(0)
        return min_element

    def sift_up(self, index):
        parent = self.get_parent(index)
        while index > 0 and self.heap[parent][1] >= self.heap[index][1]:
            if self.heap[parent][1] == self.heap[index][1] and self.heap[parent][0] < self.heap[index][0]:
                break
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = self.get_parent(index)

    def sift_down(self, index):
        left = self.get_left_child(index)
        right = self.get_right_child(index)
        if left >= self.size and right >= self.size:
            return
        if right >= self.size:
            if self.heap[left][1] == self.heap[index][1]:
                min_index = left if self.heap[left][0] < self.heap[index][0] else index
            else:
                min_index = left if self.heap[left][1] < self.heap[index][1] else index
        else:
            if self.heap[left][1] == self.heap[right][1]:
                min_index = left if self.heap[left][0] < self.heap[right][0] else right
            else:
                min_index = left if self.heap[left][1] < self.heap[right][1] else right
            if self.heap[min_index][1] == self.heap[index][1]:
                min_index = min_index if self.heap[min_index][0] < self.heap[index][0] else index
            else:
                min_index = min_index if self.heap[min_index][1] < self.heap[index][1] else index
        if min_index != index:
            self.heap[min_index], self.heap[index] = self.heap[index], self.heap[min_index]
            self.sift_up(min_index)

    def __str__(self):
        return str(self.heap)


def main():
    N, M = [int(i) for i in input().split()]
    t = [int(i) for i in input().split()]
    heap = Heap(N)
    for i in range(N):
        heap.insert([i, 0])
    # print(heap)
    curWrite = 0
    while curWrite < M:
        timeProcess = heap.extract_min()
        print(timeProcess[0], timeProcess[1])
        timeProcess[1] += t[curWrite]
        heap.insert(timeProcess)
        curWrite += 1


main()
