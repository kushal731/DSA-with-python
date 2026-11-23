class Node:
    def __init__(self, info, priority):
        self.info = info
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.que = []

    def Insert(self, n):
        for a in range(0, len(self.que)):
            if self.que[a].priority >= n.priority:
                self.que.insert(a, n)
                return
        self.que.append(n)

    def Delete(self):
        self.que.pop(0)

    def Display(self):
        for a in self.que:
            print(a.info, "-", a.priority)

# Main
n1 = Node("A", 1)
n2 = Node("B", 2)
n3 = Node("C", 3)
n4 = Node("D", 17)
n5 = Node("E", 18)
n6 = Node("M", 26)

p = PriorityQueue()
p.Insert(n1)
p.Insert(n2)
p.Insert(n3)
p.Insert(n4)
p.Insert(n5)
p.Insert(n6)

print("Priority Queue after Inserting")
p.Display()

print("Priority Queue after Deleting")
p.Delete()
p.Display()

# Graph for Asymptotic Notation
import matplotlib.pyplot as p

p.title('Priority Queue- Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y1 = [1 for y in x]
y2 = [y for y in x]

p.plot(x, y1, 'r', label='O(1)- Insert Operation')
p.plot(x, y2, 'g', label='O(n)- Delete Operations')

p.legend()
p.show()