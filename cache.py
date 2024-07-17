from doublylinkedlist import DoublyLinkedList
from node import Node

class LRUCache:
    
    def __init__(self):
        self.linkedlist = DoublyLinkedList(capacity=10)
        self.hashmap = {}

    def getList(self):
        return self.linkedlist
    
    def getTable(self):
        return self.hashmap

    def search(self, ipt):
        node = None
        key = self.linkedlist.retrieveKey(ipt)
        if key == -1:
            node = self.linkedlist.push(ipt)
            self.hashmap.update({node.getKey(): node})
        else:
            if self.hashmap[key] == self.linkedlist.getHead():
                self.linkedlist.popFirst()
            else:
                self.linkedlist.deleteFirst(ipt)
            node = self.linkedlist.push(ipt)
            self.hashmap.update({node.getKey(): node})
        curr = self.hashmap[node.getKey()]
        return curr.val
        

cachetest = LRUCache()
cachetest.search("Potato")
print(cachetest.getTable())
cachetest.search("Potato")
print(cachetest.getTable())
cachetest.search("Potato")
print(cachetest.getTable())
cachetest.search("Apple")
cachetest.search("Apple")
cachetest.search("Vanilla")
cachetest.search("Meringue")
cachetest.search("Vanilla")
cachetest.search("Apple")
cachetest.search("Pizza")
cachetest.search("Banana")
print(cachetest.getList().string())

    



    