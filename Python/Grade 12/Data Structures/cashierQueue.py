from queue import queue
from listNode2 import listNode2
class cashierQueue(queue):
    
    def insert(self, name, time):
        if self.head == None:
            self.head = listNode2(name, time)
            self.tail = self.head
        else:
            self.tail.link = listNode2(name, time)
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
            return n
    def totalTime(self):
        time = 0
        if self.head != None:
            n = self.head
            while n != None:
                time += int(n.list.valueAtIndex(1))
                n = n.link
        return time

    def printList(self):
        print "Cashier: "+ "Total: "+str(self.totalTime())+"mins"
        if self.head != None:
            n = self.head
            while n != None:
                print str(n.list.firstNode.value)+ ":  "+str(n.list.firstNode.link.value)+"min"
                n = n.link
        else:
            print "Empty"
        print
        return 0
    
            




    '''
    
    def __init__(self, value):
        for i in xrange(value):
            self.cashierList.append(queue())
    def insert(self, value):
        q = self.cashierList[0]
        time = 0
        while not q.empty:
            time += q
    '''
            



