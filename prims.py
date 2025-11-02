import heapq

def prim(n,adj):
    visited = [False] * n
    min_heap = [(0,0)]  #weight,node
    cost = 0
    mst =[]

    while min_heap:
        weight,u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        cost += weight

        for v,w in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap,(w,v))
                mst.append((u,v,w))

    return mst,cost

adj = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4)],
    3: [(1, 2), (2, 4)]
}
n = 4

mst, cost = prim(n, adj)
print("MST edges:", mst)
print("Total cost:", cost)

