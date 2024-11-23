def floyd_warshall(graph):
    nodes = list(graph.keys())
    dist = {node: {node2: float('inf') for node2 in nodes} for node in nodes}

    for node in nodes:
        dist[node][node] = 0

    for node in graph:
        for neighbor, weight in graph[node].items():
            dist[node][neighbor] = weight

    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

graph = {
    'A': {'B': 4, 'H': 8},
    'B': {'C': 8, 'H': 11},
    'C': {'D': 7, 'F': 4, 'I': 2},
    'D': {'E': 9, 'F': 14},
    'E': {'F': 10},
    'F': {'G': 2},
    'G': {'H': 1, 'I': 6},
    'H': {'I': 7},
    'I': {}
}

graph2 = {
    'A': {'B': 5, 'D': 30},
    'B': {'C': 5, 'D': 20},
    'C': {'D': 5},
    'D': {}
}

print("Floyd-Warshall Algorithm:", floyd_warshall(graph))
print("Floyd-Warshall Algorithm:", floyd_warshall(graph2))
