class MathUtils:
    @staticmethod
    def square(number: float) -> float:
        return number ** 2
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b
    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b
if __name__ == "__main__":
    print(f"Квадрат числа 4: {MathUtils.square(4)}")
    print(f"Сумма 3 и 7: {MathUtils.add(3, 7)}")
    print(f"Произведение 5 и 6: {MathUtils.multiply(5, 6)}")