class Pair:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"x is {self.x} and y is {self.y}"

    def __str__(self) -> str:
        return str(self.x) + str(self.y)


p = Pair(20, 30)

print(repr(p))
