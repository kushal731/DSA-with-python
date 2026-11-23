def dfs(graph, source):
    stack = []
    visited = []
    stack.append(source)
    visited.append(source)

    while len(stack) != 0: # Stack not equal to empty
        vertex = stack.pop()
        print(vertex, end=" ")
        for u in graph[vertex]:
            if u not in visited:
                stack.append(u)
                visited.append(u)

# Main
graph = {'A': ['B', 'D'], 'B': ['C', 'F'], 'C': ['E', 'G', 'H'], 'D': ['F'], 'E': ['B'], 'F': ['A'], 'G': ['E', 'H'], 'H': []}

print("Given Graph", graph)

print("\nDFS Traversal \n")
dfs(graph, 'H')

# Graph for Asymptotic Notation
import matplotlib.pyplot as p

p.title('DFS- Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [1 for y in x]

p.plot(x, y, 'r', label='O(V+E)- Time Complexity')
p.legend()
p.show()