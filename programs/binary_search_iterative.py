def BinarySearch(mylist, key, low, high):
    if low <= high:
        mid = (low + high) // 2
        if key == mylist[mid]:
            return mid
        elif key < mylist[mid]:
            return BinarySearch(mylist, key, low, mid-1)
        else:
            return BinarySearch(mylist, key, mid + 1, high)
    else:
        return -1

#Main
mylist = [11, 12, 13, 14, 15, 16, 17, 18]
key = int(input("Enter key "))
n = len(mylist)
pos = BinarySearch(mylist, key, 0, n-1)
if pos == -1:
    print("UnSuccessfull search")
else:
    print("Sucessfull search: Element found at : ", pos)

# Graph for Asymptotic Notation
import matplotlib.pyplot as p
import math

p.title('Binary Search Iterative- Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [math.log(y) for y in x]

p.plot(x, y, 'r', label='O(log n)- Binary Search')
p.legend()
p.show()