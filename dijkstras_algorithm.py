import heapq

def dijkstra(graph, start):
    pq = []
    heapq.heappush(pq, (0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

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

print("Dijkstra's Algorithm:", dijkstra(graph, 'A'))
print("Dijkstra's Algorithm:", dijkstra(graph2, 'A'))
