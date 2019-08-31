import queue
import random
q = queue.PriorityQueue()


class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print("New job description")

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)


q = queue.PriorityQueue()

for i in range(1, 10):
    # random.seed(1)
    q.put(random.randint(1, 100))

for i in range(1, 10):
    print(q.get())