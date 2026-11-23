from timeit import default_timer as t

def Selectionsort(s1):
    n = len(s1)
    for a in range(n-1):
        min = a
        # Find the position of minimum element
        for b in range(a+1, n):
            if s1[b] < s1[min]:
                min = b
        # swap the minimum element with correct position
        if(min != a):
            s1[a], s1[min] = s1[min], s1[a]
    return s1

# Main
s1 = [65, 4, 1, 8, 11, 23, 14, 9, 45]
print("Given List = ", s1)

start = t()
slist = Selectionsort(s1)
print("Sorted List = ", slist)
end = t()

et = (end - start) * 1000000
print(f"Execution time = {et:.2f} micoseconds")

# Graph for Asymptotic Notation
import matplotlib.pyplot as p

p.title('Selection Sort - Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [y*y for y in x]

p.plot(x, y, 'r', label='O(n**2)- Best/Average/Worst Case')

p.legend()
p.show()