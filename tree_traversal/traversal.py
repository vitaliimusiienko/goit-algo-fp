from collections import deque
from heap_visualization.visualize_heap import draw_tree


def generate_colors(n):
    colors = []
    for i in range(n):
        intensity = int(255 * (i + 1) / n)
        colors.append(f"#{intensity:02x}{100:02x}{255-intensity:02x}")
    return colors


def dfs(root):
    stack = [root]
    order = []

    while stack:
        node = stack.pop()
        order.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return order


def bfs(root):
    queue = deque([root])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return order


def visualize_traversal(root, method="dfs"):
    nodes = dfs(root) if method == "dfs" else bfs(root)
    colors = generate_colors(len(nodes))

    for node, color in zip(nodes, colors):
        node.color = color

    draw_tree(root)