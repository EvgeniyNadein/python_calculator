# Автор: Надеин Е.М., группа ПРЗ-23, 14.11.2026
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное число (используйте точку для дробей).")

def main():
    print("--- Консольный калькулятор ---")
    print("Для выхода из программы введите 'выход' вместо первого числа.")

    while True:
        print("\n--- Новое вычисление ---")

        user_input = input("Введите первое число (или 'выход'): ").strip().lower()
        if user_input == 'выход':
            print("Программа завершена. До свидания!")
            break

        try:
            num1 = float(user_input)
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное число или 'выход'.")
            continue


        num2 = get_number("Введите второе число: ")

        valid_operators = ('+', '-', '*', '/')
        while True:
            operator = input(f"Выберите операцию {valid_operators}: ").strip()
            if operator in valid_operators:
                break
            print("Ошибка: Неверная операция. Пожалуйста, выберите из списка.")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Ошибка: Деление на ноль невозможно!")
                continue
            result = num1 / num2

        if result.is_integer():
            result = int(result)

        print(f"Результат: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    main()
