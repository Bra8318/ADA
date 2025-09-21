#Topological sorting using dfs.
graph = {
    1:[2,3],
    2:[5],
    3:[4,5],
    4:[6],
    5:[4],
    6:[]
}
visited = set()
stack = []

def dfs(node):
    if node in visited:
        return 
    visited.add(node)

    for neighbor in graph[node]:
        dfs(neighbor)
    stack.append(node)

for node in graph:
    dfs(node)


print(stack[::-1])