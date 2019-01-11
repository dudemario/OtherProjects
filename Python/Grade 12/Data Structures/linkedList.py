'''
@author: aaronkilpatrick
'''

from listNode import listNode  
'''
Class linkedList is a data type which holds references to items in a list.
Items are linked to each other through a pointer to the next item in the list.
The list itself holds reference to the first item in the list and the list length.
'''
class linkedList:
    
    #Initialize a new list as empty. No nodes with no length.
    #No parameters or return values.
    def __init__(self):
        self.length = 0
        self.firstNode = None
        #self means myself - myLinkedList

    def insertNewFirstNode(self, value):
        newNode = listNode(value)

        if not self.firstNode:
            self.firstNode = newNode
        else:
            newNode.link = self.firstNode
            self.firstNode = newNode
        self.length += 1
    
    #Method creates and inserts an item into the last position of the list.
    #param Value is any value/object being stored in the list
    #no values returned.
    def insertNewLastNode(self, value):
        #create the new node to insert
        newNode = listNode(value)
        
        #if list empty new node is first node
        if not (self.firstNode):
            self.firstNode = newNode
        else:
            #locate last node in list
            p = self.firstNode
            while (p.link):
                p = p.link
            p.link = newNode
        
        #increase length by 1
        self.length += 1

    def deleteFirstNode(self):
        if self.firstNode:
            if self.firstNode.link:
                self.firstNode = self.firstNode.link
            else:
                self.firstNode = None
            self.length -= 1
    
    #Method deletes the last item in the list.
    #No param or return values.
    def deleteLastNode(self):
        #do nothing if list is empty
        if (self.firstNode):
            
            #if the list has one node, empty list and decrease length
            if not (self.firstNode.link):
                self.firstNode = None
                self.length -= 1
                
            #otherwise the list has two or more nodes
            else:
                #initialize pointers to previous and current node
                previousNode = self.firstNode
                currentNode = self.firstNode.link
                
                #advance pointers along the list until current points
                #to last item in list
                while(currentNode.link != None):
                    previousNode = currentNode
                    currentNode = currentNode.link
                
                #now previous node points to new last node in list
                #length is decreased
                previousNode.link = None
                self.length -=1
        
    #Method prints the contents of the list out one item per line.
    #No param or return values.   
    def printListItemPerline(self):
        s = ""        
        n = self.firstNode
        
        while (n):
            s += str(n.value) + " "
            n = n.link
        print s
    
    
    '''Method prints the list contents out to one line formatted [item, "string", etc]
    No paramaters or return values
    '''
    def printList(self):
        s = ""
        n = self.firstNode
        
        #iterate through list one item at a time until last item reached
        while (n):
            #check if last item in list has been reached
            #if so, do not place a comma after the item
            if n.link:
                
                #check if item is type string. If so, place it in quotations
                if type(n.value) == str:
                    s += "'" + str(n.value) + "', "
                else:
                    s+= str(n.value) + ", "
            else:
                s+= str(n.value)
                
            #advance to next item in list
            n = n.link
        
        print "[" + s + "]"
    
    '''Search the list for a given value.
    @return The listNode where the value is stored. return None if value not found.
    ''' 
    def listSearch(self, value):
        
        n = self.firstNode
        #iterate through list until end of list is reached
        while (n):
            #if value is found return it
            if (n.value==value):
                return n
            else:
                n = n.link
        #return None if end of list is reached
        return n


    '''Method appends otherList to the end of self.
    @param otherList is a linkedList that will be appended
    '''
    def concat(self, otherList):
        n = self.firstNode
        #self list has no items
        if not self.firstNode:
            self.firstNode = otherList.firstNode
            
        #self list has 1+ items
        else:
            
            #point to last item in list
            while(n.link):
                n = n.link
            
            m = otherList.firstNode
            #if m is not an empty list
            if (m != None):
                #if m has one or more items in list
                n.link = m
            else:
                n.link = None
        
        #increase list lengths       
        self.length += otherList.length
        
    def insertAfter(self, afterValue, newValue):
        if self.firstNode:
            n = self.firstNode
            while n and n.value != afterValue:
                n = n.link
            if n:
                newNode = listNode(newValue)
                newNode.link = n.link
                n.link = newNode
        
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
                    
    def peek(self):
        return self.firstNode
    
    def valueAtIndex(self, index):
        if self.firstNode:
            n = self.firstNode
            counter = 0
            while n and counter != index:
                n = n.link
                counter += 1
            if counter == index and n:
                return n.value
        return -1
    
                    
            

        
