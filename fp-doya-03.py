import heapq
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def dijkstra_steps(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    previous = {node: None for node in graph.nodes}
    distances[start] = 0

    visited = set()
    heap = [(0, start)]
    steps = []

    while heap:
        dist, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        steps.append((node, dict(distances), dict(previous)))

        for neighbor in graph.neighbors(node):
            weight = graph[node][neighbor]['weight']
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    return steps, distances, previous


def print_shortest_paths(distances, previous, start):
    print(f"Найкоротші шляхи від вершини {start}:\n")
    for target in distances:
        path = []
        current = target
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        print(f"{start} → {target}: відстань = {distances[target]}, шлях = {' → '.join(path)}")


def visualize_dijkstra(steps, G, pos):
    fig, ax = plt.subplots(figsize=(8, 6))

    def update(frame):
        ax.clear()
        node, dist_map, prev_map = steps[frame]
        colors = []
        for n in G.nodes:
            if n == node:
                colors.append('red')
            elif n in [s[0] for s in steps[:frame]]:
                colors.append('lightgreen')
            else:
                colors.append('lightgray')

        edge_colors = []
        for u, v in G.edges():
            if prev_map.get(v) == u or prev_map.get(u) == v:
                edge_colors.append('orange')
            else:
                edge_colors.append('black')

        nx.draw(G, pos, with_labels=True, node_color=colors, edge_color=edge_colors, ax=ax)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
        ax.set_title(f"Крок {frame+1}: обробляємо вершину '{node}'")

    ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=1000, repeat=False)
    plt.show()


def main():
    edges = [
        ('A', 'B', 4), ('A', 'C', 2),
        ('B', 'C', 5), ('B', 'D', 10),
        ('C', 'D', 3), ('D', 'E', 1)
    ]

    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    pos = nx.spring_layout(G, seed=42)

    start = 'A'
    steps, distances, previous = dijkstra_steps(G, start)

    print_shortest_paths(distances, previous, start)
    visualize_dijkstra(steps, G, pos)


if __name__ == "__main__":
    main()