import random
import matplotlib.pyplot as plt

def monte_carlo_dice(n_rolls: int = 10000):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(n_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        sums_count[roll_sum] += 1

    probabilities = {k: v / n_rolls for k, v in sums_count.items()}

    print("Sums and probabilities (Monte Carlo):")
    for s, p in probabilities.items():
        print(f"Sum {s}: {p:.4f}")

    plt.bar(probabilities.keys(), probabilities.values())
    plt.xlabel("Sum of two dice")
    plt.ylabel("Probability")
    plt.title(f"Monte Carlo simulation ({n_rolls} rolls)")
    plt.show()