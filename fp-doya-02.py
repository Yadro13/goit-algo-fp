import turtle

# Фрактальне дерево з використанням рекурсії
def draw_branch(t, branch_length, angle, shrink_factor, level):
    if level == 0:
        return

    # Малюємо поточну гілку
    t.forward(branch_length)

    # Зберігаємо стан (позицію і напрям)
    pos = t.pos()
    heading = t.heading()

    # Ліва гілка
    t.left(angle)
    draw_branch(t, branch_length * shrink_factor, angle, shrink_factor, level - 1)

    # Повертаємось до попередньої точки
    t.setpos(pos)
    t.setheading(heading)

    # Права гілка
    t.right(angle)
    draw_branch(t, branch_length * shrink_factor, angle, shrink_factor, level - 1)

    # Повертаємось до попередньої точки
    t.setpos(pos)
    t.setheading(heading)

# Головна функція для запуску програми
def main():

    # Запитуємо користувача про рівень рекурсії
    level = int(input("Введіть рівень рекурсії (наприклад, 6): "))

    # Ініціалізуємо вікно для малювання
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Ініціалізуємо черепашку :)
    t = turtle.Turtle()
    t.color("brown")
    t.speed("fastest")
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()

    # Малюємо фрактальне дерево із заданим рівнем рекурсії
    draw_branch(t, branch_length=100, angle=45, shrink_factor=0.6, level=level)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
