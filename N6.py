
class MathUtils:
    @staticmethod
    def square(number: float) -> float:
        return number ** 2
if __name__ == "__main__":
    print(f"Квадрат числа 4: {MathUtils.square(4)}")