import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import deque

# Клас для представлення вузла дерева
class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

# Функція для додавання ребер до графа
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Функція для візуалізації дерева на кожному кроці
def draw_tree_step(root, title="Tree"):  # single snapshot
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.clf()
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.pause(1)

# Функція для створення градієнту кольорів
def hex_color_gradient(start_color, steps):
    base_rgb = mcolors.hex2color(start_color)
    end_rgb = (1, 1, 1)  # white
    gradient = []
    for i in range(steps):
        ratio = i / (steps - 1) if steps > 1 else 0
        interpolated = tuple(base_rgb[j] + (end_rgb[j] - base_rgb[j]) * ratio for j in range(3))
        hex_color = mcolors.to_hex(interpolated)
        gradient.append(hex_color)
    return gradient

# Функція для обходу дерева в ширину (BFS) з візуалізацією
def bfs_visual(root):
    print("\n--- BFS обхід ---")
    all_nodes = []
    q = deque([root])
    while q:
        node = q.popleft()
        all_nodes.append(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    gradient = hex_color_gradient("#1296F0", len(all_nodes))

    q = deque([root])
    i = 0
    while q:
        node = q.popleft()
        node.color = gradient[i]
        print(f"Відвідано: {node.val}")
        draw_tree_step(root, title=f"BFS крок {i+1}: {node.val}")
        i += 1
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

# Функція для обходу дерева в глибину (DFS) з візуалізацією
def dfs_visual(root):
    print("\n--- DFS обхід ---")
    stack = [root]
    visited = []
    all_nodes = []
    q = deque([root])
    while q:
        node = q.popleft()
        all_nodes.append(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    gradient = hex_color_gradient("#1296F0", len(all_nodes))

    i = 0
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        node.color = gradient[i]
        print(f"Відвідано: {node.val}")
        draw_tree_step(root, title=f"DFS крок {i+1}: {node.val}")
        i += 1
        visited.append(node)
        # push right first so that left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Основна функція для побудови дерева та запуску візуалізації
def main():
    # Побудова дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    plt.ion()
    bfs_visual(root)

    # Обнуляємо кольори
    for node in [root, root.left, root.left.left, root.left.right, root.right, root.right.left]:
        node.color = "#1296F0"

    dfs_visual(root)
    plt.ioff()
    plt.show()


if __name__ == "__main__":
    main()