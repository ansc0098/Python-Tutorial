import threading


class Counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self, value=1):
        with self.lock:
            self.count += 1
            if 1 < value:
                self.increment(value - 1)


class IncrementerThread(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        for i in range(1000000):
            self.counter.increment(2)


counter = Counter()
threads = []
for i in range(2):
    thread = IncrementerThread(counter)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(counter.count)
