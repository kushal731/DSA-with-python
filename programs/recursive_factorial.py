def factorial(n):
    if (n < 0 or int(n) != n):
        return "Not defined"
    if(n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n-1)

# Main
n = eval(input("Enter the number: "))
print("Factorial of a number : ", factorial(n))

# Graph for Asymptotic Notation
import matplotlib.pyplot as p

p.title('Factorial using Recursion- Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [y for y in x]

p.plot(x, y, 'g', label='O(n)- Time/Space Complexity')
p.legend()
p.show()