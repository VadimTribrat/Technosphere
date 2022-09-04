class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRU():
    def __init__(self, size):
        self.size = size
        self._dict = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self._dict:
            ret = self._dict[key].val
            move = self._dict[key]
            move.prev.next = move.next
            move.next.prev = move.prev
            self._to_head(move)
        else:
            ret = None
        return ret

    def set(self, key, value):
        if key in self._dict:
            self._dict[key].val = value
            move = self._dict[key]
            move.prev.next = move.next
            move.next.prev = move.prev
            self._to_head(move)
        else:
            self._dict[key] = Node(key, value)
            self._to_head(self._dict[key])

        if len(self._dict) > self.size:
            remove = self.tail.prev
            self.tail.prev = remove.prev
            remove.prev.next = self.tail
            del self._dict[remove.key]
