import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list_lecture import DoublyLinkedList


class Queue:
    def __init__(self,size=0):
        self.size = size
        # Why is our DLL a good choice to store our elements?
        self.storage =  DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1 
        # print(f"added {self.storage.tail.value} to queue's tail")

    def dequeue(self):
        if self.storage.head is None:
            return None
        self.size -= 1 
        return self.storage.remove_from_head()
        

    def len(self):
        return self.size

if __name__ == "__main__":
    # ld = ListNode(45)
    # ld.insert_after(98)
    # ld.insert_before(86)
    q1 = Queue()
    q1.enqueue(100)
    q1.enqueue(101)
    q1.enqueue(105)
    # print(q1.len())
    # print(q1.storage.head.value)
    q1.dequeue()
    # print(q1.len())
    print(q1.storage.head)
