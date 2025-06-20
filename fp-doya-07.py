import random
import matplotlib.pyplot as plt
from collections import Counter
from tabulate import tabulate


def simulate_dice_rolls(n=100_000):
    results = [random.randint(1, 6) + random.randint(1, 6) for _ in range(n)]
    counter = Counter(results)
    probabilities = {}

    for total in range(2, 13):
        count = counter[total]
        prob = count / n
        probabilities[total] = (prob, count)

    return probabilities


def print_probability_table(probabilities):
    exact_probs = {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36
    }

    table = []
    for total in range(2, 13):
        prob, count = probabilities[total]
        percentage = f"{prob * 100:.2f}% ({count})"
        expected = f"{exact_probs[total] * 100:.2f}% ({exact_probs[total]:.5f})"
        table.append([total, percentage, expected])

    print(tabulate(table, headers=["Сума", "Ймовірність (Монте-Карло)", "Аналітична ймовірність"], tablefmt="github"))


def plot_probabilities(probabilities):
    totals = list(probabilities.keys())
    monte_probs = [probabilities[total][0] for total in totals]
    exact_probs = {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36
    }
    exact_values = [exact_probs[t] for t in totals]

    plt.figure(figsize=(10, 5))
    bars = plt.bar(totals, monte_probs, label="Монте-Карло", alpha=0.7)
    plt.plot(totals, exact_values, color="red", marker='o', linestyle="--", label="Аналітичні")

    # Додавання тексту всередині стовпчиків
    for bar, _ in zip(bars, totals):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height - 0.01,
                f"{height*100:.2f}%", ha='center', va='top', color='white', fontsize=9, fontweight='bold')

    # Аналітичні значення над стовпчиками
    for x, val in zip(totals, exact_values):
        plt.text(x, val + 0.003, f"{val*100:.2f}%", ha='center', va='bottom', color='darkred', fontsize=9, fontweight='bold')

    plt.xticks(totals)
    plt.xlabel("Сума на кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Порівняння Монте-Карло та аналітичних ймовірностей")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Figure_1.png")
    plt.show()


def main():
    rolls = 100_000
    probabilities = simulate_dice_rolls(rolls)
    print(f"\nСимульовано {rolls:,} кидків двох кубиків:")
    print_probability_table(probabilities)
    plot_probabilities(probabilities)


if __name__ == "__main__":
    main()