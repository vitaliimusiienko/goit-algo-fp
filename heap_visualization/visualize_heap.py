import networkx as nx
import matplotlib.pyplot as plt
from heap_visualization.node import HeapNode


def build_heap_tree(heap):
    if not heap:
        return None

    nodes = [HeapNode(v) for v in heap]

    for i in range(len(nodes)):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(nodes):
            nodes[i].left = nodes[left]
        if right < len(nodes):
            nodes[i].right = nodes[right]

    return nodes[0]


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            pos[node.left.id] = (x - 1 / 2 ** layer, y - 1)
            add_edges(graph, node.left, pos, x - 1 / 2 ** layer, y - 1, layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            pos[node.right.id] = (x + 1 / 2 ** layer, y - 1)
            add_edges(graph, node.right, pos, x + 1 / 2 ** layer, y - 1, layer + 1)

    return graph


def draw_tree(root):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}

    add_edges(tree, root, pos)

    colors = [n[1]['color'] for n in tree.nodes(data=True)]
    labels = {n[0]: n[1]['label'] for n in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos, labels=labels, node_color=colors, node_size=2500, arrows=False)
    plt.show()