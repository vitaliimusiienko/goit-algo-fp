import argparse

from linked_list.commands import register_commands as register_linked_list
from fractal.commands import register_commands as register_fractal
from graphs.commands import register_commands as register_graphs
from heap_visualization.commands import register_commands as register_heap_visualization
from tree_traversal.commands import register_commands as register_traversal
from knapsack.commands import register_commands as register_knapsack

def main():
    parser = argparse.ArgumentParser(
        description="Algorithm CLI Bot"
    )
    subparsers = parser.add_subparsers(title="Modules", dest="module")
    
    register_linked_list(subparsers)
    register_fractal(subparsers)
    register_graphs(subparsers)
    register_heap_visualization(subparsers)
    register_traversal(subparsers)
    register_knapsack(subparsers)
    
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()