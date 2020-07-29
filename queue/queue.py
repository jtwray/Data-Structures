"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
static queue or queue from array 
vs 
dynamic queue or queue from LL
queue as a built-in list requires o(n) time complexity as all items need to be shifted to add or delete from the beginning
there is a max size for a queue


2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?

   static queue or queue from array 
vs 
dynamic queue or queue from LL
queue as a built-in list(array) requires o(n) time complexity 
    --as all items may need to be shifted to if the front reached the end of the array. 
    arrays are stored as consecutive unit of memory . 
there is a max size for an array  or static queue
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self,capacity):

        self.front = self.size = 0
        self.rear= capacity -1
        self.Q=[None]*capacity
        self.capacity=capacity

        
    
    def __len__(self):
        return f'{self.size}'
        pass

    def enqueue(self, value):
        if self.size==self.capacity:
            return f'FULL'
        f'% s dequeued from queue' % str(self.Q[self.front])
        self.front = (self.front+ 1) % self.capacity
        self.Q[self.rear]= self.size + 1
        f'% s enqueued to queue' % str(item)

        pass

    def dequeue(self):
        if self.size = 0:
            return f'EMPTY'
        
        f'% s dequed from queue' % str(self.Q[self.front])
        self.front= (self.front + 1) % self.capacity
        self.size -=1

        pass

if __name__ == '__main__':   
    queue = Queue(30) 
    queue.enqueue(10) 
    queue.enqueue(20) 
    queue.enqueue(30) 
    queue.enqueue(40) 
    queue.dequeue() 


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LLQueue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,item):
        temp = Node(item)
        if  self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        if self.front is None:
            return
        temp =self.front
        self.front=temp.next

        if(self.front is None):
            self.rear is None

if __name__== '__main__': 
    q = LLQueue() 
    q.enqueue(10) 
    q.enqueue(20) 
    q.dequeue() 
    q.dequeue() 
    q.enqueue(30) 
    q.enqueue(40) 
    q.enqueue(50)  
q.dequeue()    
    print("Queue Front " + str(q.front.data)) 
    print("Queue Rear " + str(q.rear.data)) 