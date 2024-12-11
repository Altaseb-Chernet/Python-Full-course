# class person:
#     def __init__(self,name,age,id):
#         self.id=id
#         self.name=name
#         self.age=age

    
# class student(person):
#     def __init__(self, name, age,  id , block):
#         super().__init__(name, age, id)
#         self.block=block


# p1=person('abebe',23,1601534)
# print(f'name: {p1.name}, age: {p1.age},id : {p1.id}')
# s1=student('aleme',25,19837,37)
# print(f'name: {s1.name}, age: {s1.age},id : {s1.id} block: {s1.block}')






# class vehicle:
#     def fuel_efficiency(self):
#         return 'fuel efficiency'
    
# class car(vehicle):
#     def fuel_efficiency(self):
#         return 'the car is started'
    
# class bike(vehicle):
#     def fuel_efficiency(self):
#         return 'bike is going on'
    
# v1=vehicle()
# print(v1.fuel_efficiency())
# c1=car()
# print(c1.fuel_efficiency())
# b1=bike()
# print(b1.fuel_efficiency())

# polymorphism
class Animal:
    def speak(self):
        return "I make a sound."

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Animal(), Dog(), Cat()]
for animal in animals:
    print(animal.speak())
