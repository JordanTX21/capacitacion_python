class Example:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def describe(self) -> str:
        return f"Nombre: {self.name}, Valor: {self.value}"

    def increment(self, amount: int = 1) -> None:
        self.value += amount

if __name__ == "__main__":
    item = Example("Prueba", 10)
    print(item.describe())
    item.increment(5)
    print(item.describe())
