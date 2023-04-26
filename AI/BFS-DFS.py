
from queue import Queue
# Function to perform BFS traversal
def bfs(graph, start_node):
    visited = set()  # Set to keep track of visited nodes
    q = Queue()  # Queue for BFS traversal
    q.put(start_node)
    visited.add(start_node)
    
    print("Path: ")
    while not q.empty():
        node = q.get()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.put(neighbor)

# Function to perform DFS traversal
def dfs(graph, start_node):
    visited = set()  # Set to keep track of visited nodes
    stack = [start_node]  # Stack for DFS traversal

    print("Path: ")
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            for neighbor in graph[node]:
                stack.append(neighbor)

# Input graph
graph = {}
print("Enter the graph:")
while True:
    u, v = input().split()
    if u == "-1" and v == "-1":
        break
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)
print("Graph: ",graph)

start_node = input("Enter the start node: ")
print("\n\n1.BFS TRAVERSAL")
bfs(graph, start_node)
print("\n\n2.DFS TRAVERSAL")
dfs(graph, start_node)
