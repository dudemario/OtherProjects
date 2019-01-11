from listNode2 import *
class stack:
    def __init__(self):
        self.length = 0
        self.firstNode = None

    def push(self, *args):
        newNode = listNode2(*args)

        if self.firstNode == None:
            self.firstNode = newNode
        else:
            newNode.link = self.firstNode
            self.firstNode = newNode
        self.length += 1

    def pop(self):
        if self.firstNode != None:
            n = self.firstNode.value
            if self.firstNode.link != None:
                self.firstNode = self.firstNode.link
            else:
                self.firstNode = None
            self.length -= 1
            return n

    def peek(self):
        return self.firstNode.value

    def isEmpty(self):
        return self.firstNode == None

    def printStack(self):
        s = ""
        if self.firstNode != None:
            n = self.firstNode
            s+=str(n.value.value)+", "
            while n.link != None:
                n = n.link
                s += str(n.value.value)+", "
        return "["+s[:-2]+"]"

    def printStackNames(self):
        s = ""
        if self.firstNode != None:
            n = self.firstNode
            if n.value.value == 0:
                s+="left, "
            else:
                s+= "right, "
            while n.link != None:
                n = n.link
                if n.value.value == 0:
                    s+="left, "
                else:
                    s+= "right, "
        return "["+s[:-2]+"]"

    def clear(self):
        self.firstNode = None
        
    def reverse(self):
        if self.firstNode:
            if self.firstNode.link:
                prevNode = self.firstNode
                node = prevNode.link
                prevNode.link = None
                if node.link:
                    nextNode = node.link
                    while nextNode:
                        node.link = prevNode
                        prevNode = node
                        node = nextNode
                        nextNode = nextNode.link
                    node.link = prevNode
                    self.firstNode = node
                else:
                    node.link = prevNode
                    self.firstNode = node

    



