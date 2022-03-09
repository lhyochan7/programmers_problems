from collections import deque

def dfs(graph, start):
    visited, need_visit = list(), deque()
    need_visit.append(start)

    while need_visit:
        print("Need visit = ", need_visit)
        node = need_visit.pop()

        print("node = ", node)

        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
        
    return visited

def bfs(graph, start):
    visited, need_visit = list(), deque()
    need_visit.append(start)

    while need_visit:
        node = need_visit.popleft()

        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
        
    return visited

if __name__ == '__main__':
    n,m,v = map(int, input().split())

    graph = {node: [] for node in range(1,n+1)}

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)


    print(graph)

    dfs_visited = dfs(graph, v)
    bfs_visited = bfs(graph, v)

    print(dfs_visited)
    print(bfs_visited)
