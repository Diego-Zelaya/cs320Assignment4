import sys

class StackMachine:
    # constructor
    def __init__(self): #sets up other funtions after, init = array called items =[]
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        lenofitems_ = len(self.items)
        if lenofitems_ > 0:
            return self.items.pop()
        else:
            return None

    def add(self):
        addednum_ = 0
        for item1 in self.items:
            addednum_ = item1 + addednum_

        while self.items:
            self.items.pop()

        self.items.append(addednum_)

    def sub(self):
        subnum_ = int(self.items[0]) - int(self.items[1])

        while self.items:
            self.items.pop()

        self.items.append(subnum_)

    def mul(self):
        mulnum_ = int(self.items[0]) * int(self.items[1])

        while self.items:
            self.items.pop()

        self.items.append(mulnum_)

    def div(self):
        divnum_ = int(self.items[0]) / int(self.items[1])

        while self.items:
            self.items.pop()

        self.items.append(divnum_)

    def mod(self):
        modnum_ = int(self.items[0]) % int(self.items[1])

        while self.items:
            self.items.pop()

        self.items.append(modnum_)
