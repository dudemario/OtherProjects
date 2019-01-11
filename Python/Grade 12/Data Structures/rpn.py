from stack import stack as s
def add(x, y):
    return x+y
def sub(x, y):
    return x-y
def mul(x, y):
    return x*y
def div(x, y):
    return x/y
def pow(x, y):
    return x**y
operands = {"+":add,
            "-":sub,
            "*":mul,
            "/":div,
            "^":pow}
class Calc:
    def __init__(self):
        self.stack = s()
    def push(self, value):
        if type(value) == float or type(value) == int:
            self.stack.push(value)
            return self.stack.peek()
        elif value in operands:
            value2 = self.stack.pop()
            value1 = self.stack.pop()
            self.stack.push(operands[value](value1, value2))
            return self.stack.peek()
        else:
            return "Error"
    def swap(self):
        if self.stack.isEmpty != None:
            s1 = self.stack.pop()
            if self.stack.empty == None:
                self.stack.push(s1)
                return self.stack.peek()
            else:
                s2 = self.stack.pop()
                self.stack.push(s1)
                self.stack.push(s2)
                return self.stack.peek()
        else:
            return "Error"

    def disp(self):
        return self.stack.peek()
    
    def clear(self):
        self.stack.clear()
        return "Cleared"
    
    def equate(self, list):
        self.clear()
        for i in list:
            self.push(i)
        print self.disp()


