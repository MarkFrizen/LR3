import json
from typing import Any, Type
class JsonSerializer:
    @staticmethod
    def to_json(obj: Any) -> str:
        if not hasattr(obj, "__dict__"):
            raise TypeError("Объект не поддерживает сериализацию в JSON")
        return json.dumps(obj.__dict__, indent=4, ensure_ascii=False)
    @staticmethod
    def from_json(json_str: str, cls: Type[Any]) -> Any:
        data = json.loads(json_str)
        return cls(**data)
if __name__ == "__main__":
    class Person:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age
    person = Person("Иван", 30)
    json_str = JsonSerializer.to_json(person)
    print("Сериализованный JSON:")
    print(json_str)
    new_person = JsonSerializer.from_json(json_str, Person)
    print(f"\nДесериализованный объект: {new_person.name}, {new_person.age} лет")