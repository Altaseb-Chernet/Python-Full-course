# class Person:
#     def __init__(self,name,age,favorite_color):
#         self.name=name
#         self.age=age
#         self.favorite_color=favorite_color
# person1=Person('Altaseb',21,['white','yellow','green'])
# print(person1.name)
# print(person1.age)
# for i in person1.favorite_color:
#     print(i)

# class Library:
#     def __init__(self,name,location,book_title):
#         self.name=name
#         self.location=location
#         self.book_title=book_title

# library1=Library('Tesfa-gebreselassie','dbu',['fresh-module','Electrical-engineering','software-engineering'])

# library2=Library('kebede-michael','dbu',['fresh-module','Amharic','national-geography'])

# print(library1.name)
# print(library1.location)
# for i in library1.book_title:
#     print(i)

# print(library2.name)
# print(library2.location)
# for i in library2.book_title:
#     print(i)

# class Student:
#     def __init__(self,name,age,grades,courses):
#         self.name=name
#         self.age=age
#         self.grades=grades
#         self.courses=courses

# Student1=Student('abebe',21,{'python':'A','java':'B'},['java','python','react.js'])
# print(Student1.name)
# print(Student1.age)
# print(Student1.grades)
# print(Student1.courses)

# class Product:
#     def __init__(self,name,price,manufacturing_date):
#         self.name=name
#         self.price=price
#         self.manufacture=manufacturing_date

# product1=Product("laptop",3500,2024)
# print(product1.name)
# print(product1.price)
# print(product1.manufacture)
        

# class car:
#     def __init__(self,model,brand,year,service_date):
#         self.model=model
#         self.brand=brand
#         self.year=year
#         self.service=service_date

# car1=car('jhyt','htre',2024,2025)
# print(car1.brand)
# print(car1.model)
# print(car1.service)
# print(car1.year)

# class school:
#     def __init__(self,school_name,no_of_students,students_name):
#         self.name=school_name
#         self.student_name=students_name
#         self.no_students=no_of_students

# school1=school('mehal-medea',2000,{'abebe':4,'aster':3.8,'Alemu':4})
# print(school1.name)
# print(school1.student_name)
# print(school1.student_name)

class book:
    
    def __init__(self,title='the love life to death',author='Adis Alemayehu',publication_year=2024,):
        self.title=title
        self.author=author
        self.pulicate=publication_year

    def book_info(self):
        print(f'the book title is {self.title} and the autor {self.author} and the publication year is {self.pulicate}')    
book1=book()
book1.book_info()

class Animal:
    animal_name="bob"
    def __init__(self,name,species):
        self.name=name
        self.species=species
    @classmethod
    def display_animal_info(cls,name,species):
        cls.name=name
        cls.species=species
    @staticmethod
    def is_domestic(dog):

        
        
        
        



        
        