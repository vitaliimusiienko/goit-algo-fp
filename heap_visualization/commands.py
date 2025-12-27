import heapq
from heap_visualization.visualize_heap import build_heap_tree, draw_tree


def register_commands(subparsers):
    parser = subparsers.add_parser(
        "heap",
        help="Visualize binary heap"
    )

    parser.add_argument(
        "--values",
        nargs="+",
        type=int,
        required=True
    )

    parser.set_defaults(func=handle_command)


def handle_command(args):
    data = args.values

    print("Original:", data)

    heapq.heapify(data)
    print("Heap array:", data)

    root = build_heap_tree(data)
    draw_tree(root)