def dfs(graph,start):
    visited = set()
    stack = [start]

    while stack:
        cur_node = stack.pop()
        while cur_node not in visited:
            visited.add(cur_node)
            print(cur_node,end = ' ')

            for neighbor in graph[cur_node]:
                if neighbor not in visited:
                    stack.append(neighbor)


graph = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['B', 'E', 'F'],
    'E': ['D'],
    'F': ['D'],
}

dfs(graph,'A')