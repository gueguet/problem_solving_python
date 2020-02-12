from random import randrange


class StackMin():
    def __init__(self):
        self.stack = []
        self.min = []
    
    def push(self, value):
        self.stack.append(value)
        if len(self.min) == 0 or value < self.min[-1]:
            self.min.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        value = self.stack.pop()
        if value == self.min[-1]:
            self.min.pop()
        return value

    def getMin(self):
        if len(self.stack) == 0:
            return None
        if len(self.min) == 0:
            return None
        return self.min[-1]



# test 

stack = StackMin()

for i in range (5):
    stack.push(randrange(1, 200))

print("Min of {}".format(stack.stack))
print(stack.getMin())