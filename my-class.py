class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def bark(self):
        print("Bark!")

    def display_info(self):
        print(f"Dog Name: {self.name}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def display_info(self):
        print(f"Cat Name: {self.name}, Color: {self.color}")

cat = Cat("Whiskers", "Tabby")
cat.color
cat.display_info()

dog = Dog("Buddy")
dog.display_info()

jerry = Dog("Jerry")
jerry.bark()
