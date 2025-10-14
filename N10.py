class NumberSequence:
    def __init__(self, start: int, end: int, step: int = 1):
        self.start = start
        self.end = end
        self.step = step
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current
        self.current += self.step
        return result
if __name__ == "__main__":
    print("Числа от 1 до 10:")
    for num in NumberSequence(1, 10):
        print(num, end=' ')
    print()