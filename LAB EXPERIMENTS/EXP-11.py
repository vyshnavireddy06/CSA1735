colors = ["Red", "Green", "Blue"]

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

result = {}

def color_map(region):
    if region == len(graph):
        return True

    place = list(graph.keys())[region]

    for color in colors:
        if all(result.get(n) != color for n in graph[place]):
            result[place] = color

            if color_map(region + 1):
                return True

            del result[place]

    return False

if color_map(0):
    print("Map Coloring Solution:")
    for region, color in result.items():
        print(region, ":", color)
else:
    print("No solution")
