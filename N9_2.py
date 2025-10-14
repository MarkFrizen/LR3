from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> None:
        pass
class Dog(Animal):
    def make_sound(self) -> None:
        print("Гав!")
class Cat(Animal):
    def make_sound(self) -> None:
        print("Мяу!")
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    dog.make_sound()
    cat.make_sound()