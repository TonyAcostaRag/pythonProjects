from tests import TestExecutor
from dataStructures.NonLinear.trees.heaps.Heap import Heap


def heap_sort(arr):

    heap = Heap(len(arr))
    for i in range(0, len(arr)):
        heap.insert_in_heap(arr[i])

    for i in range(len(arr), 0, -1):
        arr[i-1] = heap.delete_max()
    return arr


if __name__ == '__main__':

    TestExecutor.execute_function(
        [
            [[20, 14, 2, 15, 10, 21]]
        ],
        heap_sort
    )
