class stack:
    def __init__(self, max, top):
        self.maxsize = max
        self.top = top
        self.list = []

    def push(self, data):
        if self.top == self.maxsize - 1:
            print("Stack is full")
        else:
            self.top = self.top + 1
            self.list.append(data)
            print(data, "has been added to stack")

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Popped item = ", self.list.pop())
            self.top = self.top - 1

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("contents of stack are:")
            for i in reversed(self.list):
                print(i)

# Main
s = stack(3, -1)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.display()
s.pop()
s.display()
s.pop()
s.display()
s.pop()
s.display()

# Graph for Asymptotic Notation
import matplotlib.pyplot as p

p.title('Stack - Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [1 for y in x]

p.plot(x, y, 'r', label='O(1)- Push/Pop Operation')
p.legend()
p.show()