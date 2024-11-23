def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative weight cycle")

    return distances

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

print("Bellman-Ford Algorithm:", bellman_ford(graph, 'A'))
print("Bellman-Ford Algorithm:", bellman_ford(graph2, 'A'))
