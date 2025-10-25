class Calculator:
    """Калькулятор с базовыми операциями и валидацией"""

    def __init__(self, a: float, b: float) -> None:
        self.a = self.validator(a)
        self.b = self.validator(b)

    def add(self) -> float:
        """Сложение"""
        return self.a + self.b

    def sub(self) -> float:
        """Вычитание"""
        return self.a - self.b

    def mult(self) -> float:
        """Умножение"""
        return self.a * self.b

    def div(self) -> float:
        """Деление"""
        if self.b == 0:
            raise ZeroDivisionError("На ноль делить нельзя")
        return self.a / self.b

    @staticmethod
    def validator(value: float) -> float:
        """
        Проверка аргумента: должно быть числом (int или float)
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Все элементы должны быть числами.")
        return float(value)
