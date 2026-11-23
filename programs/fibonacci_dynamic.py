memo = []

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if memo[n] != -1:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

# Main
memo = []
for i in range(10):
    memo.append(-1)

print("Fibonacci number is ", fib(6))