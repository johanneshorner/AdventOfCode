import math
import heapq

with open("input.in") as file:
    risk_level_graph = [[int(risk_level) for risk_level in line.strip()] for line in file]

def dikstra(graph):
    distances = {(x, y) : math.inf for y in range(len(graph)) for x in range(len(graph[0]))}

    distances[(0, 0)] = 0
    heap = []
    heapq.heappush(heap, (0, (0, 0)))

    while len(heap) > 0:
        distance, (x, y) = heapq.heappop(heap)
        
        if x < len(graph[0]) - 1:
            if distance + graph[y][x + 1] < distances[(x + 1, y)]:
                distances[(x + 1, y)] = distance + graph[y][x + 1]
                heapq.heappush(heap, (distances[(x + 1, y)], (x + 1, y)))
        if y < len(graph) - 1:
            if distance + graph[y + 1][x] < distances[(x, y + 1)]:
                distances[(x, y + 1)] = distance + graph[y + 1][x]
                heapq.heappush(heap, (distances[(x, y + 1)], (x, y + 1)))

    return distances[(len(graph) - 1, len(graph[0]) - 1)]

risk_level_graph = [
    [x + j + i if x + j + i <= 9 else (x + j + i) - 9 for j in range(5) for x in y]
    for i in range(5) for y in risk_level_graph
]

risk_level_graph[0][0] = 0
print(dikstra(risk_level_graph))