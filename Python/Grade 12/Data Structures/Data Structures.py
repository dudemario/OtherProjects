'''
Data Structures

How lists/args are managed in memory

A list is a space in memory that we can add to / delete from at will in Python

If in memory allocate space in memorty for two lists. Then add an item to end of list 1
Causes problem

Linkedlist might be a solution

'''

from linkedList import *
from stack import *
myList = linkedList()
myList.insertNewFirstNode(5)
myList.insertNewFirstNode(6)
myList.insertNewFirstNode(7)
myList.insertNewFirstNode(3)
myList.insertNewFirstNode(4)
myList.insertAfter(7, 1)
myList.printList()
myList.reverse()
myList.printList()
'''
myStack = stack()
myStack.push(5)
myStack.push(7)
myStack.push(6)
print myStack.pop()
myStack.push(1)
myStack.printStack()
'''
'''
Stack:
Initialize
-length (try not to ref)
-firstNode

def push(self, value):
    #insertNewFirstNode()

def pop():
    #deleteFirstNode()
    #return value

def peek():
    #return firstNode.value

def empty():
    #compare length
    #return True or False

'''
