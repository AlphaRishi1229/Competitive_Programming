class Item:
    def __init__(self, value, weight) -> None:
        self.value = value
        self.weight = weight
        self.cost = value // weight

    def __lt__(self, other):
        return self.cost < other.cost


class FractionalKnapsack:
    def fill_bag(values, weights, capacity):
        items = [Item(values[i], weights[i]) for i in range(len(weights))]
        items.sort(reverse=True)
        total_value = 0

        for item in items:
            current_weight = item.weight
            current_value = item.value

            if capacity - current_weight >= 0:
                capacity -= current_weight
                total_value += current_value
            else:
                fractional_part = capacity / current_weight
                capacity = int(capacity - (current_weight * fractional_part))
                total_value += current_value * fractional_part
                break
        return total_value

wt = [10, 40, 20, 30]
val = [60, 40, 100, 120]
capacity = 50

# Function call
maxValue = FractionalKnapsack.fill_bag(val, wt, capacity)
print("Maximum value in Knapsack =", maxValue)