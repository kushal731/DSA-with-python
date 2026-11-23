class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Function to add node in the beginning
    def AddNode(self, data):
        newnode = Node(data)
        newnode.next = self.head
        if self.head != None:
            self.head.prev = newnode
        self.head = newnode

    # Function to delete node at beginning
    def DeleteNode(self):
        temp = self.head
        # if dll is not empty
        if temp != None:
            self.head = temp.next
            self.head.prev = None

    def printList(self):
        temp = self.head
        print("\nTraversal in forward direction")
        while temp != None:
            print(temp.data, end=" ")
            last = temp
            temp = temp.next

        print("\nTraversal in reverse direction")
        while last != None:
            print(last.data, end=" ")
            last = last.prev

# Main
dll = DoublyLinkedList()
dll.AddNode(10)
dll.AddNode(15)
dll.AddNode(20)

print("Doubly Linked List after adding node")
dll.printList()

print("\n\nDoubly Linked List after deleting node")
dll.DeleteNode()
dll.printList()

# Graph for Asymptotic Notation
import matplotlib.pyplot as p

p.title('Doubly Linked List - Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [1 for y in x]

p.plot(x, y, 'r', label='O(1)- Inserting/Deleting a node')
p.legend()
p.show()