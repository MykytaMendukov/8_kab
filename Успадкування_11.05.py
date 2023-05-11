class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(self.name, 'їсть...')

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def bark(self):
        print(self.name, 'гавкає.')
    def __str__(self):
        return hotdog.name, hotdog.age, hotdog.breed
hotdog = Dog('Sharick', 3, 'Mops')

print(hotdog.name, hotdog.age, hotdog.breed)

hotdog.bark()
hotdog.eat()


