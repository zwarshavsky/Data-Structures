import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        # print(f"created new Tree with value: {self.value}")

    # Insert the given value into the tree
    def insert(self, value):
        # print(value)
        if self.value is None:
            self = BinarySearchTree(value)

        elif value < self.value:
            # print(f"{value} is less than {self.value}")
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        elif value >= self.value:
            # print(f"value is greater than or == {self.value}")
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        print(target,self.value)
        if self.value == target:
            print("base case:",self.value)
            return True

        elif target < self.value:
            if self.left == None:
                return False
            return self.left.contains(target)

        elif target >= self.value:
            if self.right == None:
                return False
            # else:
            return self.right.contains(target)



    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value    
        return self.right.get_max() 
    
    def get_min(self):
        if self.left == None:
            return self.value    
        return self.left.get_min() 
     

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        q = Queue()
        q.enqueue(self)
        while q.size != 0:
            node = q.dequeue()
            cb(node.value)
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
            


        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node == None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # line by line print out, 
        # adds nodes that are on the same line, 
        # then it starts to pop out the children
        q = Queue()
        q.enqueue(node)
        while q.size != 0:
            node = q.dequeue()
            print(node.value)
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)
        while s.size != 0:
            node = s.pop()
            print(node.value)
            if node.left:
                s.push(node.left)
            if node.right:
                s.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


if __name__ == "__main__":
    bs = BinarySearchTree(5)
    bs.insert(2)
    bs.insert(1)
    bs.insert(6)
    bs.insert(7)
    bs.insert(8)
    # print(bs.contains(7))
    # print(bs.contains(9))
    # print(bs.get_max())
    # print(bs.get_min())
    # arr = []
    # cb = lambda x: arr.append(x)
    # bs.for_each(cb)
    # bs.in_order_print(bs)
    print("bft_print:",bs.bft_print(bs))
    print("dft_print:",bs.dft_print(bs))
