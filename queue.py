class Queue:
    """
    Represents a queue data structure
    """
    def __init__(self):
        """
        constructor
        front => index for the front of the queue
        back => index of the back of the queue
        queue => list to keep track of items
        size => size of items in the queue. NOT the size of the list
        """
        self.front = 0
        self.back = 0
        self.queue = []
        self.size = 0

    def enqueue(self, value):
        """
        add the value to the end of the list.
        Increment the size and back index
        :param value:
        :return:
        """
        self.queue.append(value)
        self.back += 1
        self.size += 1

    def dequeue (self):
        """
        remove an item from the queue.
        this doesn't actually remove the item from the list, just from the queue
        :return:
        """
        self.front += 1
        self.size -= 1

    def peek(self):
        """
        peek the value at the front
        :return: value at the front index
        """
        return self.queue[self.front]


def test():
    que = Queue()
    que.enqueue(1) # queue 1
    que.enqueue(2) # queue 2
    que.enqueue(3) # queue 3
    print(que.size) # print size. 3 in this case
    print(que.peek()) #print first element. 1 in this case
    que.dequeue() # remove from front
    que.dequeue() # remove from front
    print(que.peek()) # print first element. should be 3
    print(que.size) # print size. should be 1
    que.enqueue(4) # queue 4
    que.enqueue(5) # queue 6
    print(que.peek()) # print front. should be 3
    que.dequeue() # dequeue
    print(que.peek()) # print front. should be 4
    print(que.size) #print size. should be 2
    
if __name__ == "__main__":
    test()
