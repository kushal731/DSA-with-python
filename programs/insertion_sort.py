from timeit import default_timer as t

def Insertionsort(s1):
    n = len(s1)
    for a in range(1, n):
        ele = s1[a]
        b = a - 1
        while b >= 0 and ele < s1[b]:
            s1[b+1] = s1[b]
            b = b - 1
        s1[b+1] = ele
    return s1

# Main
s1 = [65, 4, 1, 8, 11, 23, 14, 9, 45]
print("Given List = ", s1)

start = t()
slist = Insertionsort(s1)
print("Sorted List = ", slist)
end = t()

et = (end - start) * 1000000
print(f"Execution time = {et:.2f} micoseconds")

# Graph for Asymptotic Notation
import matplotlib.pyplot as p

p.title('Insertion Sort - Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y1 = [y for y in x]
y2 = [y*y for y in x]

p.plot(x, y1, 'r', label='O(n)- Best Case')
p.plot(x, y2, 'g', label='O(n**2)- Average/Worst Case')

p.legend()
p.show()