class BST:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Insert method to create nodes
    def insert(self, data):
        if self.data == None:
            return

        if data < self.data:
            if self.left == None:
                self.left = BST(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = BST(data)
            else:
                self.right.insert(data)

    # Search method
    def search(self, data):
        if self.data == data:
            print("Node is present in the tree")
        elif data < self.data:
            if self.left == None:
                print("Node is not present in the tree")
            else:
                self.left.search(data)
        else:
            if self.right == None:
                print("Node is not present in the tree")
            else:
                self.right.search(data)

    # Methods to traverse tree
    def inorder(self):
        if self.left != None:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right != None:
            self.right.inorder()

    def preorder(self):
        print(self.data, end=" ")
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()

    def postorder(self):
        if self.left != None:
            self.left.postorder()
        if self.right != None:
            self.right.postorder()
        print(self.data, end=" ")

# Main
root = BST(21)
list1 = [30, 10, 5, 12, 25, 100, 3, 7]
for i in list1:
    root.insert(i)

print("\n\nTraversal - inorder")
root.inorder()
print("\n\nTraversal - preorder")
root.preorder()
print("\n\nTraversal - postorder")
root.postorder()

root.search(71)

# Graph for Asymptotic Notation
import matplotlib.pyplot as p
import math

p.title('BST- Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [math.log(y) for y in x]

p.plot(x, y, 'r', label='O(log n)- Insert/Delete/Search Operation')
p.legend()
p.show()