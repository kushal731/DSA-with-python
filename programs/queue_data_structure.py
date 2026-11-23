def Enqueue():
    if len(que) == size: # check whether queue is full or not
        print("Queue is Full!!!!")
    else:
        element = input("Enter the element:")
        que.append(element)
        print(element, "is added to the Queue!")

def dequeue():
    if len(que) == 0: # Check whether queue is empty or not
        print("Queue is Empty!!!")
    else:
        ele = que.pop(0)
        print("element removed!!:", ele)

def display():
    print("Contents of queue : ", que)

# Main
que = []
size = int(input("Enter the size of Queue:"))
while True:
    print("Select the Operation: 1.Add 2.Delete 3.Display 4.Quit")
    choice = int(input())
    if choice == 1:
        Enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid Option!!!")

# Graph for Asymptotic Notation
import matplotlib.pyplot as p

p.title('Queue- Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [y for y in x]

p.plot(x, y, 'r', label='O(1)- Enqueue/Dequeue Operations')
p.legend()
p.show()