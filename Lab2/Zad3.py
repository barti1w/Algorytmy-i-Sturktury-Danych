import Zad1
class Queue:
    def __init__(self):
        self.Queue=Zad1.LinkedList()

    def __repr__(self):
        tmp=self.Queue.head
        ret=f'{tmp.value}'
        while(tmp.next):            
            tmp=tmp.next
            ret = ret + ', ' f'{tmp.value}'
        return ret

    def peek (self):
        return self.Queue.head.value

    def enqueue (self, value):
       self.Queue.append(value)

    def dequeue (self):
            # tmp=self.Queue.head.value
            # self.Queue.head=self.Queue.head.next
            # return tmp
        return self.Queue.pop()
        
    def __len__(self):
        return len(self.Queue)

queue = Queue()
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
client_first=queue.dequeue()
print(len(queue))
assert client_first == 'klient1'
assert len(queue) == 2
print(queue)