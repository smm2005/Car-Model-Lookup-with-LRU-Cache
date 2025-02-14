from doublylinkedlist import DoublyLinkedList
from node import Node

class LRUCache:
    
    def __init__(self, c=10):
        self.linkedlist = DoublyLinkedList(capacity=c)
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
        

    



    