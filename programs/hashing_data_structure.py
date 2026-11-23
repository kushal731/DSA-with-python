hashtable = [[] for x in range(10)]

def display():
    for i in range(len(hashtable)):
        print(i, end=" ")
        for j in hashtable[i]:
            print("-->", end=" ")
            print(j, end=" ")
        print()

def insert(key, value):
    k = key % len(hashtable)
    hashtable[k].append(value)

# Main
insert(10, "Kishor")
insert(25, "Sandeep")
insert(20, "Uday")
insert(9, "Chandan")
insert(21, "Karan")
insert(15, "Tarun")
insert(16, "Bharath")

print("Hashtable")
display()

# Graph for Asymptotic Notation
import matplotlib.pyplot as p

p.title('Hashing- Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y1 = [1 for y in x]
y2 = [y**2 for y in x]

p.plot(x, y1, 'r', label='O(1)- Inserting value')
p.plot(x, y2, 'g', label='O(n**2)- Displaying value')
p.legend()
p.show()