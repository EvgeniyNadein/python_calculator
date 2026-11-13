def add(a: float, b: float) -> float:
    """Складывает два числа."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Вычитает второе число из первого."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Умножает два числа."""
    return a * b

def divide(a: float, b: float) -> float:
    """
    Делит первое число на второе.
    Вызывает ValueError, если делитель равен 0.
    """
    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a / b

def power(base: float, exponent: float) -> float:
    """Возводит первое число (основание) в степень второго числа."""
    return base ** exponent

def modulo(a: float, b: float) -> float:
    """
    Возвращает остаток от деления первого числа на второе.
    Вызывает ValueError, если делитель равен 0.
    """
    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a % b
