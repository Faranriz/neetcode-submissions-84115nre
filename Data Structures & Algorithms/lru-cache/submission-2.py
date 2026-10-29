class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}     #map key to node

        # left = LRU, rigth = MRU
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    #remove node
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next


    #insert node at back of list to become MRU node
    def insert(self, node):
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
