class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
            
class LRUCache:
    


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.least = Node(0,0)
        self.most = Node(0,0)
        
        self.least.next = self.most
        self.most.prev = self.least
        

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        
            
    def insert(self, node):
        prev_mru = self.most.prev
        node.prev = prev_mru
        prev_mru.next = node
        self.most.prev = node
        node.next = self.most
        
        

        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:   
            self.remove(self.cache[key])
            
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.least.next
            self.remove(lru)
            del self.cache[lru.key]
            
                            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)