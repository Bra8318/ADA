"""from collections import deque
def dfs(graph,start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return result


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(graph,'A')"""

visited = []
queue =[]
def bfs(visited,graph,start):
    visited.append(start)
    queue.append(start)

    while queue:
        x = queue.pop(0)
        print(x,end=' ')

        for neighbor in graph[x]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
bfs(visited,graph,'A')

