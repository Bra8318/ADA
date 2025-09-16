graph = {}
def add_vertex(vertex):
    if vertex in graph:
        print(f"{vertex} already exist")
    graph[vertex] = []

def add_edge(v1,v2):
    if v1 not in graph or v2 not in graph:
        print("Vertex not found")
        return
    graph[v1].append(v2)
    graph[v2].append(v1)


add_vertex('A')
add_vertex('B')
add_vertex('C')
add_vertex('D')
add_vertex('E')

add_edge('A','B')
add_edge('A','C')
add_edge('B','D')
add_edge('C','D')
add_edge('C','E')

print(graph)

