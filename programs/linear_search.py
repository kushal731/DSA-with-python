from timeit import default_timer as t

def LinearSearch(s1, key):
    n = len(s1)
    for a in range(0, n):
        if s1[a] == key:
            return a
    return -1

# Main
s1 = [1, 3, 5, 4, 7, 9]
print("Given list is ", s1)

key = int(input("Enter key to be searched : "))

start = t()
pos = LinearSearch(s1, key)

if pos == -1:
    print("Element not found: Unsuccesfull search")
else:
    print("Element found: Succesfull search")

end = t()
et = (end - start) * 1000000
print(f"Execution time = {et:.2f} micoseconds")

# Graph
import matplotlib.pyplot as p

p.title("Linear Search - Graph for Asymptotic Notation")
p.xlabel("Input Size")
p.ylabel("Steps")

x = list(range(1, 100))
y1 = [y for y in x]
y2 = [1 for y in x]
p.plot(x, y1, 'r', label='O(n)- Worst/Average case')
p.plot(x, y2, 'b', label='O(1) - Best Case')

p.legend()
p.show()