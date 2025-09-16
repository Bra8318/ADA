#using Greedy Graph Coloring.
def graph_color(graph):
    colored = {}
    for vertex in graph:
        neighbor_color = set()
        for neighbor in graph[vertex]:
            if neighbor in colored:
                neighbor_color.add(colored[neighbor])
        color = 0
        while color in neighbor_color:
            color += 1
        colored[vertex] = color
    return colored

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

result = graph_color(graph)
print("Bipartite graph coloring is: ",result)
