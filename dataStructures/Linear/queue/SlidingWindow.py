class SlidingWindow:

    def __init__(self, size: int):
        self.slicing_window = []
        self.window_capacity = size

    def next(self, val: int) -> float:
        
        self.slicing_window.append(val)
        if len(self.slicing_window) > self.window_capacity:
            self.slicing_window.pop(0)

        return sum(self.slicing_window) / len(self.slicing_window)
    

if __name__ == '__main__':

    answers = []
    my_slicing_window = SlidingWindow(3)
    answers.append(None)
    print('Window instantiation:', answers[-1])

    answers.append(my_slicing_window.next(1))
    print('Insert first num:', answers[-1])
    print(my_slicing_window.slicing_window)

    answers.append(my_slicing_window.next(10))
    print('Insert second num:', answers[-1])
    print(my_slicing_window.slicing_window)

    answers.append(my_slicing_window.next(3))
    print('Insert third num:', answers[-1])
    print(my_slicing_window.slicing_window)

    answers.append(my_slicing_window.next(5))
    print('Insert fourth num:', answers[-1])
    print(my_slicing_window.slicing_window)

    answers.append(my_slicing_window.next(10))
    print('Insert fourth num:', answers[-1])
    print(my_slicing_window.slicing_window)
