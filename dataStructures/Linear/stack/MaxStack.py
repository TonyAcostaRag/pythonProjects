class MaxStack_ArrayMaxPairs:
    
    def __init__(self):
        self.stack = []

    def push(self, val) -> None:
        if len(self.stack) > 0:
            current_max = self.stack[-1][1]
            self.stack.append((val, max(current_max, val)))
        else:
            self.stack.append((val, val))
            
    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMax(self) -> int:
        return self.stack[-1][1]
    

class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_tracker_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.max_tracker_stack or val > self.max_tracker_stack[-1][0]:
            self.max_tracker_stack.append([val, 1])
        elif val == self.max_tracker_stack[-1][0]:
            self.max_tracker_stack[-1][1] += 1

    def pop(self):
        if not self.stack:
            return
        
        if self.max_tracker_stack[-1][0] == self.stack[-1]:

            if self.max_tracker_stack[-1][1] > 1:
                self.max_tracker_stack[-1][1] -= 1
            else:
                self.max_tracker_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMax(self):
        return self.max_tracker_stack[-1][0]


if __name__ == '__main__':

    expected_results = [None, None, None, None, 8, None, 4, 6]
    results = []
    my_max_stack = MaxStack()
    results.append(None)
    results.append(my_max_stack.push(6))
    results.append(my_max_stack.push(4))
    results.append(my_max_stack.push(8))
    results.append(my_max_stack.getMax())
    results.append(my_max_stack.pop())
    results.append(my_max_stack.top())
    results.append(my_max_stack.getMax())
    
    for i in range(len(results)):

        if results[i] == expected_results[i]:
            print('TC:', i, 'PASSED')
        else:
            print('TC:', i, 'FAILED - Actual:', results[i], '- Expected:', expected_results[i])
