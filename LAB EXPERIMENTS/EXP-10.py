import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

h = {'A': 4, 'B': 3, 'C': 1, 'D': 0}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            return path, g

        if node in visited:
            continue
        visited.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                heapq.heappush(
                    pq, (new_g + h[neighbor],
                         new_g, neighbor,
                         path + [neighbor])
                )

    return None, float('inf')

path, cost = astar('A', 'D')
print("Path:", path)
print("Cost:", cost)
