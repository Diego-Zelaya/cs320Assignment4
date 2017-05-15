import sys

class StackMachine:
    # constructor
    def __init__(self): #sets up other funtions after, init = array called items =[]
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def add(self):
        AddedNum = 0
        for item1 in self.items:
            AddedNum = item1 + AddedNum

        while self.items:
            self.items.pop()

        self.items.append(AddedNum)


    def sub(self):
        SubNum = 0
        for item1 in self.items:
            SubNum = SubNum - item1

        while self.items:
            self.items.pop()

        self.items.append(SubNum)


'''
    def mul(self):
        self.items.mul()

    def div(self):
        self.items.div()

    def mod(self):
       self.items. div()
'''


testing = StackMachine()
testing.push(11)
testing.push(3)
testing.sub()

test2 = testing.add()

print("finnished...")
# 1, push

