from listNode2 import listNode2
class queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    def insert(self, value):
        if self.head == None:
            self.head = listNode2(value)
            self.tail = self.head
        else:
            self.tail.link = listNode2(value)
            self.tail = self.tail.link
        self.length += 1
    def remove(self):
        if self.head != None:
            n = self.head
            if self.head.link != None:
                self.head = self.head.link
            else:
                del self.head
                self.head = None
                self.tail = None
            self.length -= 1
            return n.value
            
    def empty(self):
        return self.head == None

    def printList(self):
        s = ""
        if self.head != None:
            n = self.head
            while n != None:
                s += str(n.value)+ ", "
                n = n.link
        return "["+s[:-2]+"]"

    def peek(self):
        return self.head.value

'''
myQueue = queue()
myQueue.insert(5)
myQueue.insert(6)
myQueue.insert(7)
print myQueue.printList()
print myQueue.remove()
print myQueue.remove()
'''


