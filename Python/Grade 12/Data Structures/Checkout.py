from cashierQueue import cashierQueue
from queue import queue
from linkedList import linkedList
fIn = open("customers.txt")
allCashiers = linkedList()
for i in xrange(6):
    allCashiers.insertNewLastNode(cashierQueue())
customers = cashierQueue()
for line in fIn:
    customer = line.strip().split("\t")
    customers.insert(" ".join(customer[:2]), customer[2])
#print customers.remove().list.valueAtIndex(1)
while not customers.empty():
    minTime = 2147483647
    minIndex = 0
    cashier = allCashiers.firstNode
    for i in xrange(6):
        if cashier.value.totalTime() == 0:
            minIndex = i
            break
        if minTime > cashier.value.totalTime():
            minTime =  cashier.value.totalTime()
            minIndex = i
        cashier = cashier.link
    cashier = allCashiers.valueAtIndex(minIndex)
    customer = customers.remove()
    customerName = customer.list.valueAtIndex(0)
    customerTime = customer.list.valueAtIndex(1)
    cashier.insert(customerName, customerTime)
    cashier = allCashiers.firstNode
for i in xrange(6):
    cashier.value.printList()
    cashier = cashier.link
print "---------------------------"

