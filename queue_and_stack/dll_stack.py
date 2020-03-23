import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list_lecture import DoublyLinkedList

class Stack:
    def __init__(self,size=0):
        self.size = size
        # Why is our DLL a good choice to store our elements?
        self.storage =  DoublyLinkedList()

    def push(self, value):
        #adding to head is expensive for a singly linked list, but for doubly linked
        #list it is an identical process
        self.storage.add_to_tail(value)
        self.size += 1 
        print(f"added {self.storage.tail.value} to the stack's tail")

    def pop(self):
        print(self.storage.remove_from_tail(),"removed")
        self.size -= 1 

    def len(self):
        return self.size

if __name__ == "__main__":
    s1 = Stack()
    s1.push(20)
    s1.push(25)
    s1.push(26)
    print(s1.len()) 
    print(s1.storage.tail.value) 
    s1.pop() 
    print(s1.len()) 
    print(s1.storage.tail.value)
