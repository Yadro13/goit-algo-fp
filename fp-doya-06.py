# Цей код реалізує два алгоритми для вирішення задачі про рюкзак:
# жадібний алгоритм та динамічне програмування.
# Обидва алгоритми приймають словник страв з їх вартістю та калорійністю,
# а також бюджет, і повертають список вибраних страв, загальну вартість та калорійність.

# Жадібний алгоритм 
def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_cost = 0
    total_calories = 0
    selected = []

    for name, props in sorted_items:
        if total_cost + props['cost'] <= budget:
            selected.append(name)
            total_cost += props['cost']
            total_calories += props['calories']

    return selected, total_cost, total_calories

# Динамічне програмування 
def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]['cost']
        cal = items[name]['calories']
        for b in range(budget + 1):
            if cost > b:
                dp[i][b] = dp[i - 1][b]
            else:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + cal)

    result = []
    b = budget
    total_cost = 0
    total_calories = dp[n][budget]
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = names[i - 1]
            result.append(name)
            b -= items[name]['cost']
            total_cost += items[name]['cost']

    result.reverse()
    return result, total_cost, total_calories

# Основна функція для запуску алгоритмів
if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100

    greedy_result, greedy_cost, greedy_cals = greedy_algorithm(items, budget)
    print("Greedy Algorithm Result:")
    print("Страви:", greedy_result)
    print("Загальна вартість:", greedy_cost)
    print("Загальна калорійність:", greedy_cals)

    dp_result, dp_cost, dp_cals = dynamic_programming(items, budget)
    print("\nDynamic Programming Result:")
    print("Страви:", dp_result)
    print("Загальна вартість:", dp_cost)
    print("Загальна калорійність:", dp_cals)