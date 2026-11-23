class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def AddNode(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def iterate(self):
        temp = self.head
        while(temp != None):
            val = temp.data
            temp = temp.next
            yield val

# Main
L1 = Linkedlist()
L1.AddNode(5)
L1.AddNode(15)
L1.AddNode("Hello")
L1.AddNode(45)

print("Linked List")
for val in L1.iterate():
    print(val, end="-->")
print("Null")

# Graph for Asymptotic Notation
import matplotlib.pyplot as p

p.title('Singly Linked List Iterators- Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [1 for y in x]

p.plot(x, y, 'r', label='O(1)- Inserting/Deleting a node')
p.legend()
p.show()