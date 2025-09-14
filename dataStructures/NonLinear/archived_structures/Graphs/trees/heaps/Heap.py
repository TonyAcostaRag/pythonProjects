class Heap:

    def __init__(self, max_size):
        self._max_size = max_size + 1
        self._current_size = 0
        self._data = [-1] * self._max_size

    def insert_in_heap(self, element):
        if self._current_size == self._max_size:
            print('Heap is full!')
            return
        self._current_size += 1
        heap_index = self._current_size

        while heap_index > 1 and element > self._data[heap_index//2]:
            self._data[heap_index] = self._data[heap_index//2]
            heap_index //= 2
        self._data[heap_index] = element

    def delete_max(self):
        if self._current_size == 0:
            print('Heap is empty!')
            return

        element = self._data[1]
        self._data[1] = self._data[self._current_size]
        self._data[self._current_size] = -1
        self._current_size -= 1
        i = 1
        j = i * 2
        while j <= self._current_size:
            if self._data[j + 1] > self._data[j]:
                j += 1
            if self._data[j] > self._data[i]:
                temp = self._data[j]
                self._data[j] = self._data[i]
                self._data[i] = temp
                i = j
                j = i * 2
            else:
                break
        return element

    def get_max(self):
        if self._current_size == 0:
            print('Heap is empty!')
            return
        return self._data[1]

    def get_heap_len(self):
        return len(self._data)

    def get_data(self):
        return self._data

    def is_empty(self):
        return len(self._data) == 0


if __name__ == '__main__':
    h = Heap(6)
    h.insert_in_heap(25)
    h.insert_in_heap(14)
    h.insert_in_heap(2)
    h.insert_in_heap(20)
    h.insert_in_heap(10)
    h.insert_in_heap(40)
    print(h.get_data())
    print(h.delete_max())
    print(h.get_data())
    print(h.delete_max())
    print(h.get_data())
    print(h.delete_max())
    print(h.get_data())
    print(h.delete_max())
    print(h.get_data())
    print(h.delete_max())
    print(h.get_data())
    print(h.delete_max())
    print(h.get_data())

    import heapq as heap

    print('\nHeap by using heapq inbuilt python module:')
    L1 = []
    L2 = [20, 4, 2, 90, 45, 4, 14]
    heap.heappush(L1, 25)
    heap.heappush(L1, 14)
    heap.heappush(L1, 2)
    heap.heappush(L1, 20)
    heap.heappush(L1, 10)
    heap.heappush(L1, 40)
    print(L1)
    e = heap.heappop(L1)
    print(e)
    print(L1)
    e = heap.heappushpop(L1, 1)
    print(e)
    print(L1)
    e = heap.heapreplace(L1, 1)
    print(e)
    print(L1)

    print('\nConverting a list into a heap:')
    print(L2)
    heap.heapify(L2)
    print(L2)
