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
        return self.name

hotdog = Dog('Sharick', 3, 'Mops')

print(hotdog.name, hotdog.age, hotdog.breed)
print(hotdog)
hotdog.bark()
hotdog.eat()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def __str__(self):
        return super().__str__() + f' , student_id: {self.student_id}'

student1 = Student('Oleg', 46, '32er34')

with open('info_studebt.txt', 'w') as file:
    file.write(str(student1))


