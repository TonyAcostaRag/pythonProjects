class RecentCounter:

    def __init__(self):
        self.counter_queue = []

    def ping(self, t: int) -> int:

        while self.counter_queue and self.counter_queue[0] < (t - 3000):
            self.counter_queue.pop(0)
        
        self.counter_queue.append(t)
        
        return len(self.counter_queue)
    

if __name__ == '__main__':

    recent_calls = RecentCounter()
    print(recent_calls.ping(1))
    print(recent_calls.ping(100))
    print(recent_calls.ping(3001))
    print(recent_calls.ping(3002))
