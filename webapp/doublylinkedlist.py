from node import Node

class DoublyLinkedList:

    k = 0

    def __init__(self, capacity):
        self.head = None
        self.capacity = capacity

    def push(self, v):
        node = Node(key=self.k, val=v, prev=None, next=None)
        if not self.head:
            self.head = node
        else:
            self.head.setPrev(node)
            node.setNext(self.head)
            self.head = node
        if self.length() > self.capacity:
            self.pop()
        self.k += 1
        return self.head
    
    def pop(self):
        curr = self.head
        while curr:
            if curr.next.next == None:
                saved = curr.next
                curr.next = None
            curr = curr.next
        return saved.val
    
    def popFirst(self):
        saved = self.head.val
        self.head = self.head.next
        return saved
    
    def deleteFirst(self, val):

        temp = self.head
        if temp != None:
            if temp.val == val:
                self.head = self.head.next
                self.head.prev = None
                return
        while temp:
            if temp.val == val:
                break
            prev = temp
            temp = temp.next
        
        if temp == None:
            return
        prev.next = temp.next
        temp.next.setPrev(prev)
        temp = None

    
    def retrieveKey(self, value):
        curr = self.head
        while curr:
            if curr.val == value:
                return curr.getKey()
            curr = curr.next
        return -1
    
    def getHead(self):
        return self.head
    
    def length(self):
        curr = self.head
        n = 0
        while curr:
            n += 1
            curr = curr.next
        return n
    
    def string(self):
        string = ""
        curr = self.head
        while curr:
            if curr.next == None:
                string += "{}".format(curr.val)
                break
            else:
                string += "{} --> ".format(curr.val)
            curr = curr.next
        return string
            
    
dll = DoublyLinkedList(capacity=100)

dll.push(1)
dll.push(1)
dll.push(3)
dll.push(4)
dll.push(5)
dll.push(6)
dll.popFirst()
print(dll.string())
