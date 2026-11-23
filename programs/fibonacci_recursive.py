def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Main
n = eval(input("Enter the number : "))
if (n < 0 or int(n) != n):
    print("Please enter positive integer")
else:
    print("Fibonacci Series :")
    for i in range(0, n):
        print(fib(i), end=" ")

# Graph for Asymptotic Notation
import matplotlib.pyplot as p

p.title('Fibonacci Recursive- Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [2**y for y in x]

p.plot(x, y, 'r', label='O(2^n)- Recursive Fibonacci')
p.legend()
p.show()