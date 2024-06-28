class Computer:

    def __init__(self) -> None:
        self.name = "Nirav"
        self.age = 19

    def update(self):
        self.age = 30

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()

if c1.compare(c2):
    print("They are same")
c1.update()
c1.name = "Kalpesh"
print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)