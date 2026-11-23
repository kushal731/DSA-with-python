from timeit import default_timer as t

def BinarySearch(s1, key, low, high):
    if low <= high:
        mid = (low + high) // 2
        if key == s1[mid]:
            return mid
        elif key < s1[mid]:
            return BinarySearch(s1, key, low, mid-1)
        else:
            return BinarySearch(s1, key, mid+1, high)
    else:
        return -1

# Main
s1 = [11, 21, 34, 44, 52, 66, 73, 88]
print("Given List = ", s1)

key = int(input("Enter key "))

n = len(s1)
start = t()
pos = BinarySearch(s1, key, 0, n-1)

if pos == -1:
    print("Unsuccessfull Search: Key not found")
else:
    print("Successfull Search: Key found at :", pos)
end = t()
et = (end - start) * 1000000
print(f"Execution time = {et:.2f} micoseconds")

# Graph for Asymptotic Notation
import matplotlib.pyplot as p
import math

p.title('Binary Search - Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y1 = [1 for y in x]
y2 = [math.log(y, 2) for y in x]

p.plot(x, y1, 'r', label='O(1)- Best Case')
p.plot(x, y2, 'b', label='O(log n)- Average/Worst Case')

p.legend()
p.show()