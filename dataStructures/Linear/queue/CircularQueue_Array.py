import threading
import time
from datetime import datetime


class CircularQueue:

    def __init__(self, queue_capacity):
        self.circular_queue = [0] * queue_capacity
        self.queue_capacity = queue_capacity
        self.queue_length = 0
        self.frontIndex = 0
        self.queueLock = threading.Lock()

    def enqueue(self, value):
        with self.queueLock:
            if self.queue_length == self.queue_capacity:
                return False
            
            self.circular_queue[(self.frontIndex + self.queue_length) % self.queue_capacity] = value
            time.sleep(.1)
            self.queue_length += 1
        return True
    
    def dequeue(self):
        if self.queue_length == 0:
            return False
        
        self.frontIndex = (self.frontIndex + 1) % self.queue_capacity
        self.queue_length -= 1
        return True
    
    def Front(self):
        if self.queue_length == 0:
            return -1
        
        return self.circular_queue[self.frontIndex]

    def Rear(self):
        if self.queue_length == 0:
            return -1
        
        return self.circular_queue[(self.frontIndex + self.queue_length - 1) % self.queue_capacity]
    
    def isEmpty(self):
        return self.queue_length == 0
    
    def isFull(self):
        return self.queue_length == self.queue_capacity
    
    def display_values(self):
        print(self.circular_queue)
        

if __name__ == '__main__':

    '''
    param = []
    my_circular_queue = CircularQueue(3)
    print('Queue real length:', len(my_circular_queue.circular_queue))
    print('Queue functional length:', my_circular_queue.queue_length)
    my_circular_queue.display_values()
    param.append(my_circular_queue.enqueue(1))
    my_circular_queue.display_values()
    param.append(my_circular_queue.enqueue(2))
    my_circular_queue.display_values()
    param.append(my_circular_queue.enqueue(3))
    my_circular_queue.display_values()
    param.append(my_circular_queue.enqueue(4))
    print('Trying to add the 4...', param[-1])
    param.append(my_circular_queue.Rear())
    print('Rear:', param[-1])
    param.append(my_circular_queue.isFull())
    print('Is queue full?', param[-1])
    print('Front:', my_circular_queue.Front())
    print('Dequeuing...')
    param.append(my_circular_queue.dequeue())
    print('Front:', my_circular_queue.Front())
    print('Rear:', my_circular_queue.Rear())
    print('Displaying the queue values...')
    my_circular_queue.display_values()
    print('Is queue full?', my_circular_queue.isFull())
    print('Queue functional length:', my_circular_queue.queue_length)
    print('Queue real length:', len(my_circular_queue.circular_queue))
    param.append(my_circular_queue.enqueue(4))
    my_circular_queue.display_values()
    param.append(my_circular_queue.Rear())
    print(param[-1])
    

    expected_results = [True,True,True,False,3,True,True,True,4]
    for i in range(len(param)):

        if param[i] == expected_results[i]:
            print('Param', i+1, 'PASSED - Expected:', expected_results[i], 'Result:', param[i])
        else:
            print('Param', i+1, 'FAILED - Expected:', expected_results[i], 'Result:', param[i])
    '''

    start_time = datetime.now()
    my_circular_queue = CircularQueue(10)
    def enqueue_value(circular_queue, values):
        for value in values:
            circular_queue.enqueue(value)

    value_num = 100
    thread_one = threading.Thread(target=enqueue_value, args=[my_circular_queue, [i + 101 for i in range(value_num)]])
    thread_two = threading.Thread(target=enqueue_value, args=[my_circular_queue, [i + 201 for i in range(value_num)]])
    thread_three = threading.Thread(target=enqueue_value, args=[my_circular_queue, [i + 301 for i in range(value_num)]])

    thread_one.start()
    thread_two.start()
    thread_three.start()

    thread_one.join()
    thread_two.join()
    thread_three.join()

    print('Multithreading execution done!')
    print(my_circular_queue.circular_queue)
    end_time = datetime.now() - start_time
    print('---> Thread-safe elapsed time:', end_time)
