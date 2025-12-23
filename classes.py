class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def __init__(self, doggy):
        self.doggy = doggy
    def intro(self):
        print(f"Hi, my name is {self.doggy}!")
    def bark(self):
        print("Bhau Bhau")


class Cat(Mammal):
    def __init__(self, kitty):
        self.kitty = kitty
    def intro(self):
        print(f"Hi, my name is {self.kitty}!")
    def meow(self):
        print("Meow Meow")


doggy = Dog("Bruno")
doggy.bark()
doggy.intro()

kitty = Cat("Luna")
kitty.meow()
kitty.intro()