import queue

q = queue.PriorityQueue()


class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print("New job description")
    
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

q = queue.PriorityQueue()
