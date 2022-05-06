# A Stack is a special kind of collection

class Stack:
    def __init__(self, size):
        if isinstance(size, int) and size > 0:
            self.maxSize=size
            self.content=[]
        else:
            raise Exception("Wrong stack size given")
    def __str__(self):
        return f"({len(self)}/{self.maxSize}) {self.content}"
    def __len__(self):
        return len(self.content)
    def __eq__(self, other):
        return self.maxSize == other.maxSize and self.content == other.content
    def __contains__(self, value): # in
        return value in self.content
    def push(self, value):
        if len(self) >= self.maxSize: #The stack is full
            raise Exception("Stack full!")
        else:
            self.content.append(value)
    def pop(self):
        if len(self)==0: # the stack is empty
            raise Exception("Stack empty!!")
        else:
            return self.content.pop()
    def peek(self):
        if len(self)==0: # the stack is empty
            raise Exception("Stack empty!!")
        else:
            return self.content[-1]
    def clear(self):
        self.content.clear()
    def isEmpty(self):
        return len(self)==0
    def extend(self, newSize):
        if isinstance(newSize, int) and newSize > self.maxSize:
            self.maxSize=newSize
        else:
            raise Exception("Wrong stack size given")

if __name__ == "__main__":
   
    s1=Stack(10) # 10 is the maximum size of the Stack
    s1.push(24)
    s1.push(27)
    s1.push(29)
    print(s1) # (3/10) [24,27,29]
    if 56 in s1:
        print("56 is in the Stack")
    top=s1.pop()
    print(top) # 29
    print(s1) # (2/10) [24,27]
    print(len(s1)) # 2
    top=s1.pop()
    print(top) # 27
    print(s1) # (1/10) [24]
    s2=Stack(20) # 10 is the maximum size of the Stack
    s2.push(24)
    print(s2)
    print(s1==s2)
    
    for e in s1:
        print(e)

