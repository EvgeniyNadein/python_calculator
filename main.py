# Автор: Надеин Е.М., группа ПРЗ-23, 14.11.2026
import calc_logic
from typing import Optional

def get_number(prompt: str) -> Optional[float]:
    """
    Запрашивает у пользователя число с обработкой ошибок.
    Возвращает None, если пользователь ввел 'выход'.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == "выход":
            return None
        try:
            return float(user_input)
        except ValueError:
            print("Ошибка: введите корректное число или 'выход'!")

def main():
    print("=== Модульный Калькулятор v2.0 ===")
    print("Для завершения работы введите 'выход' на любом этапе.\n")

    while True:
        num1 = get_number("Введите первое число: ")
        if num1 is None:
            break

        num2 = get_number("Введите второе число: ")
        if num2 is None:
            break

        operation = input("Выберите операцию (+, -, *, /, **, %): ").strip().lower()
        if operation == "выход":
            break

        try:
            if operation == '+':
                result = calc_logic.add(num1, num2)
            elif operation == '-':
                result = calc_logic.subtract(num1, num2)
            elif operation == '*':
                result = calc_logic.multiply(num1, num2)
            elif operation == '/':
                result = calc_logic.divide(num1, num2)
            elif operation == '**':
                result = calc_logic.power(num1, num2)
            elif operation == '%':
                result = calc_logic.modulo(num1, num2)
            else:
                print("Неизвестная операция! Попробуйте снова.\n")
                continue

            print(f"Результат: {result}\n")

        except ValueError as e:
            print(f"Ошибка вычисления: {e}\n")

    print("Работа калькулятора завершена.")

if __name__ == "__main__":
    main()
