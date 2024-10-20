
"""
["LRUCache", "put",  "put", "get", "put", "get", "put",  "get", "get", "get"]
[[2],        [1, 1], [2, 2], [1],  [3, 3], [2],  [4, 4],  [1],   [3],   [4]]

LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


self.capacity = capaci
self.cache = <map>int->int
self.used = deque
[1 => 2 => 4 => 3]


get(key): self.cache[key]
put(key): 


self.capacity = capaci
self.cache = <map>int->ListNode
self.used = ListNode
self.lru = ListNode
capacity = 4
[1 => 2 => 4 => 3]


get(key): self.cache[key].val
put(key): 
link(key): 
remove_lru()


Plan
Initialize these,
capacity
used for most-recently-used should probably use mru :)
initialize lru as it's next

head of linkedlist will be mru.next

cache<map>{int->node}.
Node -> value, prev, next.
Stop initialize.

For get, don't forget, if the key is not in cache, return -1.
If it is, make the key's node the mru, return the node's value.

For put, if the value is in cache, no need to check for capacity.
if in cache, change the node's value, make it the mru
if not in cache, check for capacity.
if capacity full, call remove_lru.
do this whether capacity filled or not:
make the new one mru - you might be able to use make_mru function, so the code might be simpler

function for making mru
get the node from key (or you can pass in the key... maybe!)
save it's next as hold_next
save it's previous as hold_previous.
set it's next to the linkedlist's head
set hold_previous' next to hold_next,
set hold_next's previous to hold_previous.


function for removing lru
You'd have to have been saving the lru node somehow.
get lru's prev as previous_lru.
set previous_lru's next to none.
Rest.


There should be edge cases / conditionals or whatever for these.
"""

class ListNode:
    def __init__(self, val=0, prev=None, next=None, key=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.key = key

    def __repr__(self):
        return f"|({self.prev if self.prev is None else self.prev.val})<=({self.val})=>({self.next if self.next is None else self.next.val})|"

class LRUCache:

    def __init__(self, capacity: int):
        self.CAPACITY = capacity
        self.mru = None
        self.lru = self.mru
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.make_mru(key)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.make_mru(key)
            self.cache[key].val = value
            return None

        if len(self.cache) == self.CAPACITY:
            self.remove_lru()

        node = ListNode(value, key=key)
        self.cache[key] = node

        if self.mru is None:
            self.lru = self.mru = node
            return None

        node.next = self.mru
        self.mru.prev = node

        if self.mru.next is None:
            self.lru = self.mru

        self.mru = node

    def make_mru(self, key: int) -> None:
        # You know, you might want to call variables 'parent' and 'child' :)
        node = self.cache[key]
        if node == self.mru:
            return

        # Saving next and previous
        hold_next = node.next
        hold_previous = node.prev

        # Making node the mru
        node.next = self.mru
        self.mru.prev = node

        # Changing node's previous' next to former node's next
        hold_previous.next = hold_next
        if hold_next is not None:  # 'is not None' eliminates the need for a comment :)
            hold_next.prev = hold_previous
        else:  # node was the lru, make it's parent the lru
            self.lru = hold_previous

        self.mru = node

    def remove_lru(self):
        del self.cache[self.lru.key]
        lru_previous = self.lru.prev
        self.lru = lru_previous
        if lru_previous is None:  # Node is lone, node is mru also (...cries...)
            self.mru = lru_previous  # No more recently used => None
            return  # self.mru and self.lru basically reinstantiated
        lru_previous.next = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
