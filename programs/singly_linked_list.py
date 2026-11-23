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

    def DeleteNode(self):
        # Store head node
        temp = self.head
        # If head node is empty
        if (temp != None):
            self.head = temp.next

    def Search(self, key):
        temp = self.head
        while temp != None:
            if temp.data == key:
                return True
            else:
                temp = temp.next
        return False

    def Display(self):
        temp = self.head
        while temp != None:
            print(temp.data, end="->")
            temp = temp.next
        print("Null")

# Main
L1 = Linkedlist()
L1.AddNode(5)
L1.AddNode(15)
L1.AddNode(35)
L1.AddNode(45)
print("Linked List after adding :")
L1.Display()
L1.DeleteNode()
print("Linked List after deleting :")
L1.Display()
res = L1.Search(10)
if res == True:
    print("Searching : Element present")
else:
    print("Searching : Element Not present")

# Graph for Asymptotic Notation
import matplotlib.pyplot as p

p.title('Singly Linked List - Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y1 = [1 for y in x]
y2 = [y for y in x]

p.plot(x, y1, 'r', label='O(1)- Inserting/Deleting a node')
p.plot(x, y2, 'b', label='O(n)- Search/Display Nodes')

p.legend()
p.show()