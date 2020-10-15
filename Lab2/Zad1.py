from typing import Any
class Node:    
    value: Any
    next: 'Node'
    def __init__(self,value,next=None):
        self.value=value
        self.next=next 
    
class LinkedList:    
    head: Node
    tail: Node
    def __init__(self):
        self.head=None
        self.tail=None
        
    def push(self, value):
        Nd=Node(value)
        Nd.next = self.head
        self.head=Nd
        
    def append(self,value):
        Nd=Node(value)
        if self.head is None:
            self.head= Nd        
        tmp = self.head 
        while (tmp.next!=None): 
            tmp = tmp.next
        tmp.next=Nd

    def node(self,index):
        tmp=self.head        
        while(tmp.next!=None and index!=1):
            index-=1
            tmp=tmp.next
        return tmp.value

    def insert(self,value,index):
        Nd=Node(value)
        tmp=self.head
        while(tmp.next!=None and index!=1):
            index-=1
            tmp=tmp.next
        Nd.next=tmp.next
        tmp.next=Nd
    
    def pop(self):
        tmp=self.head
        znacz=tmp
        tmp=tmp.next
        self.head=tmp
        return znacz
        
    def remove_last(self):
        tmp=self.head
        while (tmp.next.next!=None): 
            tmp = tmp.next
        znacz=tmp.next
        tmp.next=None
        return znacz

    def remove(self, index):
        tmp=self.head
        while(index!=1):
            index-=1
            tmp=tmp.next
        tmp.next=tmp.next.next

    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.value) 
            temp = temp.next

    def __repr__(self):
        tmp=self.head
        ret=f'{tmp.value}'
        while(tmp.next):            
            tmp=tmp.next
            ret = ret + ' -> ' f'{tmp.value}'
        return ret


    def __len__(self):
        i=1
        tmp=self.head
        while(tmp.next!=None):
            tmp=tmp.next
            i+=1
        return i


list_ = LinkedList()
assert list_.head == None
list_.push(1) 
list_.push(0)
list_.push(2)
list_.push(3)
list_.append(9)
list_.append(10)
list_.insert(5,2)
list_.pop()
list_.remove_last()
list_.remove(2)
list_.printList()
print(list_)
print(len(list_))
#print(list_.node(2))
