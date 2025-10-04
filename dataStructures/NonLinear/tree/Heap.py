class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        
        left_child_index = self._left_child(index)
        right_child_index = self._right_child(index)
        max_value_index = None
        
        while ( 
            (left_child_index < len(self.heap) and self.heap[index] < self.heap[left_child_index]) or
            (right_child_index < len(self.heap) and self.heap[index] < self.heap[right_child_index])
        ):

            if left_child_index < len(self.heap) and right_child_index < len(self.heap) and self.heap[left_child_index] >  self.heap[index] and self.heap[right_child_index] > self.heap[index]:
                max_value_index = left_child_index if self.heap[left_child_index] > self.heap[right_child_index] else right_child_index
            
            elif left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[index]:
                max_value_index = left_child_index
                
            elif right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[index]:
                max_value_index = right_child_index
            
            if max_value_index:
                self._swap(index, max_value_index)
            
            index = max_value_index
            left_child_index = self._left_child(index)
            right_child_index = self._right_child(index)            
                       
    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value
    

if __name__ == '__main__':

    myheap = MaxHeap()
    myheap.insert(95)
    myheap.insert(75)
    myheap.insert(80)
    myheap.insert(55)
    myheap.insert(60)
    myheap.insert(50)
    myheap.insert(65)

    print(myheap.heap)
    myheap.remove()
    print(myheap.heap)
    myheap.remove()
    print(myheap.heap)
