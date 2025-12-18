import pulp


def solve():
    WATER = 100
    SUGAR = 50
    LEMON_JUICE = 30
    FRUIT_PUREE = 40

    # Продукція
    lemonade = pulp.LpVariable("Лимонад", lowBound=0, cat="Integer")
    fruit_juice = pulp.LpVariable("Фруктовий_сік", lowBound=0, cat="Integer")

    # Витрати
    water = 2 * lemonade + 1 * fruit_juice
    sugar = 1 * lemonade
    lemon_juice = 1 * lemonade
    fruit_puree = 2 * fruit_juice

    model = pulp.LpProblem("Загальна_кількість", pulp.LpMaximize)
    model += lemonade + fruit_juice
    model += water <= WATER
    model += sugar <= SUGAR
    model += lemon_juice <= LEMON_JUICE
    model += fruit_puree <= FRUIT_PUREE
    status = model.solve()

    if status == pulp.LpStatusOptimal:
        print(f"Лимонад: {pulp.value(lemonade)} од.")
        print(f"Фруктовий сік: {pulp.value(fruit_juice)} од.")
        print(f"Загальна кількість продукції: {pulp.value(model.objective)} од.")

        print("Загальні витрати:")
        print(f" - вода: {pulp.value(water)} / {WATER} од.")
        print(f" - цукор: {pulp.value(sugar)} / {SUGAR} од.")
        print(f" - лимонний сік: {pulp.value(lemon_juice)} / {LEMON_JUICE} од.")
        print(f" - фруктове пюре: {pulp.value(fruit_puree)} / {FRUIT_PUREE} од.")

    else:
        print("Рішення не знайдено")


if __name__ == "__main__":
    solve()
