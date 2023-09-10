class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

        
class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.capacity = capacity
        self.current = 0
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.store:
            node = self.store[key]
            self.removeNode(node)
            self.addToHead(node)
            return node.value
        else:
            return -1

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addToHead(self, node):
        head_next = self.head.next
        head_next.prev = node
        node.next = head_next
        self.head.next = node
        node.prev = self.head
    
    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            node.value = value
            self.removeNode(node)
            self.addToHead(node)
            return
        
        if self.current != self.capacity:
            node = ListNode(key, value)
            self.store[key] = node
            self.addToHead(node)
            self.current += 1
        else:
            lru_node = self.tail.prev
            del self.store[lru_node.key]
            self.removeNode(lru_node)
            node = ListNode(key, value)
            self.addToHead(node)
            self.store[key] = node
                


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)