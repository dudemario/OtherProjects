from queue import queue
from math import *
l = [314, 15, 9265, 3, 589, 793, 23, 846, 26, 4, 3, 38, 32, 79, 50, 28, 84, 197, 1, 69, 399, 37, 51, 58, 209, 74, 9445, 92, 307, 8, 16, 40, 62, 86,  2, 0, 89, 9, 8628, 348, 25342, 117, 0, 67, 98214, 8086, 51, 32, 823, 0664, 709, 38446, 9, 55, 58, 2231, 72, 53, 59, 4081, 28481,  1174, 502, 8, 4102, 7019, 38, 52, 1155, 59, 64, 46, 22, 94, 8, 9549, 3038, 19644, 2881, 975, 6, 65, 93, 3446, 12, 847, 564, 8, 2, 337, 867, 8316, 52, 7, 120, 199, 14, 56, 4, 856, 692, 34, 60, 348, 6, 14]
radixDict = dict()
for i in xrange(10):
    radixDict[i]=queue()
def insert(r, value, digit):
    if (value/pow(10, digit))< 1:
        r[0].insert(value)
    else:
        r[floor((value/pow(10, digit))%10)].insert(value)
def remove(r, digit, l):
    q = r[digit]
    while not q.empty():
        l.append(q.remove())
for i in xrange(int(floor(log(max(l), 10))+1)):
    while len(l) != 0:
        insert(radixDict, l.pop(0), i)
    for digit in xrange(10):
        remove(radixDict, digit, l)
    #print l
print l

    
