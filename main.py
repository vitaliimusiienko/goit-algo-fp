import argparse

from linked_list.commands import register_commands as register_linked_list

def main():
    parser = argparse.ArgumentParser(
        description="Algorithm CLI Bot"
    )
    subparsers = parser.add_subparsers(title="Modules", dest="module")
    
    register_linked_list(subparsers)
    
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

def show_menu():
    print("/n=====Algorithm Bot Menu=====")
    print("1.Singly linked list")
    print("2.Pythagorean fractal")
    print("3.Dijkstra's algorithm")
    print("4.Heap visualization")
    print("5.Visualization of binary tree traversal")
    print("6.Calories (Greedy vs DP)")
    print("7.Monte Carlo (cubes)")
    print("8.Exit")