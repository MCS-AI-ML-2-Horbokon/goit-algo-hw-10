import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Визначення функції
def f(x):
    return np.sin(x) * x


def draw(a: float, b: float):
    x = np.linspace(a-0.5, b+0.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, "r", linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(f"Графік інтегрування f(x) = sin(x) * x від {a} до {b}")
    plt.grid()
    plt.show()


def integrate_monte_carlo(min_x: float, max_x: float, count: int):
    x = np.linspace(min_x, max_x, 400)
    y = f(x)
    min_y = min(y)
    max_y = max(y)
    points = np.random.uniform(low=[min_x, min_y], high=[max_x, max_y], size=(count, 2))
    k = np.sum(points[:, 1] < f(points[:, 0])) # Кількість точок під графіком (векторизовано)
    return (max_x - min_x) * (max_y - min_y) * k / count


if __name__ == "__main__":
    # Визначте межі інтегрування, наприклад, від 0 до 1
    a = 0  # нижня межа
    b = 3  # верхня межа

    # Обчислення інтеграла
    sp_area, sp_error = spi.quad(f, a, b)
    print(f"Інтеграл: {sp_area:.4f} ± {sp_error}")

    # Обчислення інтеграла методом Монте-Карло
    for n in [10_000, 100_000, 1_000_000, 10_000_000]:
        mc_area = integrate_monte_carlo(a, b, count=n)
        print(f"Інтеграл методом Монте-Карло: {mc_area:.4f} ({n} точок)")

    draw(a, b)
