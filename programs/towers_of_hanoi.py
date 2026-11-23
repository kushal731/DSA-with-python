def towerofhanoi(disk, source, aux, target):
    if(disk == 1):
        print("Move disk 1 from rod {} to rod {}".format(source, target))
        return
    towerofhanoi(disk-1, source, target, aux)
    print("Move disk {} from rod {} to rod {}".format(disk, source, target))
    towerofhanoi(disk-1, aux, source, target)

# Main
disk = int(input("Enter the number of disk: "))
towerofhanoi(disk, 'A', 'B', 'C')

# Graph for Asymptotic Notation
import matplotlib.pyplot as p

p.title('Tower of Hanoi- Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 10))
y1 = [y for y in x]
y2 = [2**y for y in x]

p.plot(x, y1, 'r', label='O(n)- Space Complexity')
p.plot(x, y2, 'g', label='O(2**n)- Time Complexity')
p.legend()
p.show()