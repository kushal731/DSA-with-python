from timeit import default_timer as t

def mergesort(s1):
    if len(s1) > 1:
        # Finding the mid of the List
        mid = len(s1) // 2
        # Dividing the List into 2 halves
        Left = s1[:mid]
        Right = s1[mid:]
        mergesort(Left)
        mergesort(Right)
        # Merge Left and Right List
        i = j = k = 0
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                s1[k] = Left[i]
                i = i + 1
                k = k + 1
            else:
                s1[k] = Right[j]
                j = j + 1
                k = k + 1
        # Checking if any element Left
        while i < len(Left):
            s1[k] = Left[i]
            i = i + 1
            k = k + 1
        while j < len(Right):
            s1[k] = Right[j]
            j = j + 1
            k = k + 1
    return s1

# Main
s1 = [65, 4, 1, 8, 11, 23, 14, 9, 45]
print("Given List = ", s1)

start = t()
slist = mergesort(s1)
print("Sorted List = ", slist)
end = t()

et = (end - start) * 1000000
print(f"Execution time = {et:.2f} micoseconds")

# Graph for Asymptotic Notation
import matplotlib.pyplot as p
import math

p.title('Merge Sort - Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [y * math.log(y, 2) for y in x]

p.plot(x, y, 'r', label='O(nlog(n))- Best/Average/Worst Case')

p.legend()
p.show()