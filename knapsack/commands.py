from knapsack.food_selection import greedy_algorithm, dynamic_programming, items

def register_commands(subparsers):
    parser = subparsers.add_parser(
        "knapsack",
        help="Select food to maximize calories within budget"
    )
    parser.add_argument(
        "--budget",
        type=int,
        required=True,
        help="Maximum budget to spend"
    )
    parser.add_argument(
        "--method",
        choices=["greedy", "dp"],
        required=True,
        help="Algorithm to use: greedy or dynamic programming"
    )
    parser.set_defaults(func=handle_command)


def handle_command(args):
    if args.method == "greedy":
        selected = greedy_algorithm(args.budget)
    else:
        selected = dynamic_programming(args.budget)

    total_cost = sum(cost for _, cost in selected)
    total_calories = sum(items[name]["calories"] for name, _ in selected)

    print(f"\nSelected items ({args.method}):")
    for name, cost in selected:
        cal = items[name]["calories"]
        print(f"{name}: cost={cost}, calories={cal}")

    print(f"\nTotal cost: {total_cost}")
    print(f"Total calories: {total_calories}")