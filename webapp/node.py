class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def getKey(self):
        return self.key
    
    def getValue(self):
        return self.val
    
    def getPrev(self):
        return self.prev
    
    def getNext(self):
        return self.next
    
    def setKey(self, k):
        self.key = k

    def setValue(self, v):
        self.val = v

    def setPrev(self, previous):
        self.prev = previous

    def setNext(self, node):
        self.next = node