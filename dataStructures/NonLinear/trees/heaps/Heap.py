class Heap:

    def __init__(self):
        self._max_size = 16
        self._current_size = 0
        self._data = [-1] * self._max_size

    def insert_in_heap(self, element):
        if self._current_size == self._max_size:
            print('No space in heap!')
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
        while j < self._current_size:
            if self._data[j] < self._data[j + 1]:
                j += 1
            if self._data[i] < self._data[j]:
                temp = self._data[i]
                self._data[i] = self._data[j]
                self._data[j] = temp
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


h = Heap()
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
