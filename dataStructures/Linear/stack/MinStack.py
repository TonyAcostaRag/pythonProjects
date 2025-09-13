class MinStack_ArrayMinPairs:

    def __init__(self):
        self.stack = []

    def push(self, val) -> None:
        if len(self.stack) > 0:
            current_min = self.stack[-1][1]
            self.stack.append((val, min(current_min, val)))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
    
    def getMin(self) -> int:
        return self.stack[-1][1]
    

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_tracker_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_tracker_stack or val < self.min_tracker_stack[-1][0]:
            self.min_tracker_stack.append([val, 1])
        elif val == self.min_tracker_stack[-1][0]:
            self.min_tracker_stack[-1][1] += 1

    def pop(self):
        if not self.stack:
            return
        
        if self.stack[-1] == self.min_tracker_stack[-1][0]:
            if self.min_tracker_stack[-1][1] > 1:
                self.min_tracker_stack -= 1
            else:
                self.min_tracker_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self):
        return self.min_tracker_stack[-1][0]
    

if __name__ == '__main__':

    expected_results = [None, None, None, None, -3, None, 0, -2]
    results = []
    my_min_stack = MinStack()
    results.append(None)
    results.append(my_min_stack.push(-2))
    results.append(my_min_stack.push(0))
    results.append(my_min_stack.push(-3))
    results.append(my_min_stack.getMin())
    results.append(my_min_stack.pop())
    results.append(my_min_stack.top())
    results.append(my_min_stack.getMin())

    for i in range(len(results)):

        if results[i] == expected_results[i]:
            print('TC:', i, 'PASSED')
        else:
            print('TC:', i, 'FAILED - Actual:', results[i], '- Expected:', expected_results[i])
