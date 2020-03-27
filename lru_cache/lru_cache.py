from doubly_linked_list_lecture import *

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit 
        self.current_number_nodes = 0 
        self.cache = DoublyLinkedList()
        self.cache_dict = {}


# limit = 3

# 1. add 3 items to master / cache

#   Master = [1] [2] [3]
#   Cache = [1] [2] [3]


# 2. add 1 item to master / Cache

# Master = [0] [1] [2] [3]

# Cache = [0] [1] [2]

# 3a. search for item 3. Not found in Cache, so will look in Master 

# a. look up value for item 3 in Master
# b. found value in item 3 in Master
# c. key value retrieved from Master for item 3 
# d. update cache with item 3 by adding to head / remove tail (least recently used) item 2

# 3b. search for item 2. found in Cache

# a. move item 2 to head (most recently used)

# Cache = [2] [0] [1]




    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):  


# node = self.storage.head  # 
# while node:  # Loop through nodes
#     ...
#     node = node.next  # Iterate

        if key in self.cache_dict.keys():
            node = self.cache.head
            while node:
                if node.value == key:
                    print("found!")
                    self.cache.move_to_front(node)
                    break
                else:
                    node = node.next
            return self.cache_dict[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if self.current_number_nodes == 0:
            self.cache.add_to_head(key)
            self.cache_dict.update({key:value})
            self.current_number_nodes += 1 

        elif self.current_number_nodes > 0 and self.current_number_nodes < self.limit:
            if key in self.cache_dict.keys():
                self.cache_dict[key] = value
                while node:
                    if node.value == key:
                        print("found!")
                        self.cache.move_to_front(node)
                        break
                    else:
                        node = node.next
            else:
                # self.storage.add_to_head({key,value})
                self.cache.add_to_head(key)
                self.cache_dict.update({key:value})
                self.current_number_nodes += 1 

        else:
            #only scenario where the item would not be in cache, but would be present in
            #master is where the cache reached max capacity and the item was previously removed
        
            if key in self.cache_dict.keys():
                self.cache_dict[key] = value
                node = self.cache.head
                while node:
                    if node.value == key:
                        print("found!")
                        self.cache.move_to_front(node)
                        break
                    else:
                        node = node.next
            else:
                temp_key = self.cache.remove_from_tail()
                del self.cache_dict[temp_key]
                self.cache_dict.update({key:value})
                self.cache.add_to_head(key)



if __name__ == "__main__":
    l = LRUCache(3)
    l.set('item1', 'a')
    l.set('item2', 'b')
    l.set('item3', 'c')
    l.set('item2','z')
    print(l.cache.head.value)
    print(l.get('item2'))
    # print(l.cache_dict)
