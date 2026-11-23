from queue import Queue

def bfs(graph, source):
    que = Queue()
    visited = []
    que.put(source)
    visited.append(source)

    while not que.empty():
        vertex = que.get()
        print(vertex, end=" ")
        for u in graph[vertex]:
            if u not in visited:
                que.put(u)
                visited.append(u)

# Main
graph = {'A': ['B', 'D'], 'B': ['C', 'F'], 'C': ['E', 'G', 'H'], 'D': ['F'], 'E': ['B'], 'F': ['A'], 'G': ['E', 'H'], 'H': []}

print("Given Graph", graph)

print("\nBFS Traversal \n")
bfs(graph, 'H')

# Graph for Asymptotic Notation
import matplotlib.pyplot as p

p.title('BFS- Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y = [1 for y in x]

p.plot(x, y, 'r', label='O(V+E)- Time Complexity')
p.legend()
p.show()