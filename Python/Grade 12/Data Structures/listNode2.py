from linkedList import linkedList
class listNode2:
    def __init__(self, *args):
        self.list = linkedList()
        for i in args:
            self.list.insertNewLastNode(i)
        self.value = self.list.peek()
        self.link = None
    def __repr__(self):
        return self.list.firstNode.link.value
