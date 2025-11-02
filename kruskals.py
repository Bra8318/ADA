def disjointSet(n):
    global parent,rank
    parent = list(range(n))
    rank = [0] * n

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u,v):
    root_u = find(u)
    root_v = find(v)

    if root_u == root_v:
        return False
    
    if rank[root_u] <= rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u]> rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1
    return True

def kruskal(n,edges):
    disjointSet(n)
    edges.sort()
    mst = []
    total_weight = 0

    for weight,u,v in edges:
        if union(u,v):
            mst.append((u,v,weight))
            total_weight += weight

    return mst,total_weight

#edges = weight , u, v
edges = [
    (1, 0, 1),
    (3, 0, 2),
    (2, 1, 2),
    (4, 1, 3),
    (5, 2, 3)
]
n = 4

mst, cost = kruskal(n, edges)
print("MST edges:", mst)
print("Total cost:", cost)

