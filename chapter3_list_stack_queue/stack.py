class MyStack():
    def __init__(self):
        self.size = 0
        self.STACK_SIZE = 100
        self.stack = [0] * self.STACK_SIZE
        self.top = self.STACK_SIZE
    
    def pop(self):
        data = self.stack[self.top]
        self.top += 1
        self.size -= 1
        return data

    def push(self, data):
        self.top -= 1
        self.stack[self.top] = data
        self.size += 1

    def get_size(self):
        return self.size
        

if __name__ == "__main__":
    s = MyStack()
    s.push(5)
    s.push(6)
    print(s.pop())
    print(s.pop())