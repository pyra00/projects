class Cat:
    name2='Tweet'
    bird1=name2
    name = 'Max'
    cat1=name

cat1=Cat.cat1
bird1=Cat.bird1
print(cat1,bird1)

#Program 2

class Student:
    name = 'Azir'

print(Student.name)

class Book:
    title = 'The Odyssey'
print(Book.title)

class Car:
    brand = 'Lexus'
print(Car.brand)

# Program 3

class Car:
    brand = 'Lexus'
    year = 2021
print(Car.brand)
print(Car.year)


class Movie:
    title = 'The Odyssey'
    year = 2026
print(Movie.title)
print(Movie.year)

class Employee:
    name = 'Drequan'
    Dept = "Instructor"
print(Employee.name)
print(Employee.Dept)

#Program 4
class Dog:
    def bark(self):
        print('Wooof!')
    
dog1 = Dog()
dog1.bark()

class Robot:
    def walk(self):
        print('The robot is walking!')

robot1=Robot()
robot1.walk()

#Program 5
class Fruit:
    name = 'Blackberry'
    def show_fruit(self):
        print(self.name)
fruit1=Fruit()
fruit1.show_fruit()

class Animals:
    species = 'Arachnids'
    def show_species(self):
        print(self.species)
animal1=Animals()
animal1.show_species()

#Program 6

class Teacher:
    def __init__(self, name):
        self.name =name 
teacher1 = Teacher('Rogger')
print(teacher1.name)

class Phone:
    def __init__(self,name):
        self.name = name
model1 = Phone('Galaxy S27')
print(model1.name)

#Program 7


class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
model1 = Laptop('MacBook', 2000)
model2 = Laptop('Hp',1500)
print(model1.brand,model1.price)
print(model2.brand,model2.price)


class Cities:
    def __init__(self, city_name, population):
        self.city_name = city_name
        self.population = population
city1 =Cities('Tampa', 1500000)
city2 =Cities('Pinellas',960000)
city3 =Cities('Pasco County',600000)
city4 =Cities('Hernado County',200000)

Cities=[city1,city2,city3,city4]
total_pop = 0
for i in Cities:
    total_pop += i.population
print(total_pop)

print(city1.city_name,city1.population)
print(city2.city_name,city2.population)
print(city3.city_name,city3.population)


# Program 8

# Exercise 1
class Player:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print('My name is', self.name)

player1 = Player('Alex')
player1.introduce()

# Exercise 2
class Pet:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print('My pet is', self.name)

pet1 = Pet('Max')
pet1.introduce()



# Program 9

# Exercise 1
class Book:
    def __init__(self, title):
        self.title = title

book1 = Book('Harry Potter')
book2 = Book('Percy Jackson')
book3 = Book('The Hobbit')

print(book1.title)
print(book2.title)
print(book3.title)

# Exercise 2
class Teacher:
    def __init__(self, name):
        self.name = name

teacher1 = Teacher('Mr. Smith')
teacher2 = Teacher('Mrs. Davis')
teacher3 = Teacher('Mr. Johnson')
teacher4 = Teacher('Ms. Wilson')

print(teacher1.name)
print(teacher2.name)
print(teacher3.name)
print(teacher4.name)



# Program 10

# Exercise 1
class Car:
    def __init__(self, brand):
        self.brand = brand

car1 = Car('Toyota')
car2 = Car('Ford')
car3 = Car('Honda')
car4 = Car('Chevy')
car5 = Car('BMW')

cars = [car1, car2, car3, car4, car5]

for car in cars:
    print(car.brand)

# Exercise 2
class Fruit:
    def __init__(self, name):
        self.name = name

fruit1 = Fruit('Apple')
fruit2 = Fruit('Banana')
fruit3 = Fruit('Orange')
fruit4 = Fruit('Grape')

fruits = [fruit1, fruit2, fruit3, fruit4]

for fruit in fruits:
    print(fruit.name)



# Program 11

# Exercise 1
class Robot:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print('Hello, I am robot', self.name)

robot1 = Robot('R2D2')
robot2 = Robot('C3PO')
robot3 = Robot('Wall-E')
robot4 = Robot('Eve')

robots = [robot1, robot2, robot3, robot4]

for robot in robots:
    robot.greet()

# Exercise 2
class Student:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print('Hello, my name is', self.name)

student1 = Student('John')
student2 = Student('Mary')
student3 = Student('David')
student4 = Student('Sarah')
student5 = Student('Mike')

students = [student1, student2, student3, student4, student5]

for student in students:
    student.introduce()



# Program 12

# Exercise 1
class Book2:
    def __init__(self, title):
        self.title = title

book1 = Book2('Dune')
book1.title = 'Dune Messiah'
print(book1.title)

# Exercise 2
class Phone:
    def __init__(self, model):
        self.model = model

phone1 = Phone('iPhone 13')
phone1.model = 'iPhone 15'
print(phone1.model)



# Program 13

# Exercise 1
class Speaker:
    def talk(self, message):
        print(message)

speaker1 = Speaker()
speaker1.talk('Testing one two')
speaker1.talk('Hello world')
speaker1.talk('Python is fun')

# Exercise 2
class Calculator:
    def show(self, number):
        print(number)

calc1 = Calculator()
calc1.show(10)
calc1.show(25)
calc1.show(100)



# Program 14

# Exercise 1
class Employee:
    def __init__(self, name):
        self.name = name

employees = []
employees.append(Employee('Alice'))
employees.append(Employee('Bob'))
employees.append(Employee('Charlie'))
employees.append(Employee('Diana'))
employees.append(Employee('Evan'))

for emp in employees:
    print(emp.name)

# Exercise 2
class Movie:
    def __init__(self, title):
        self.title = title

movies = []
movies.append(Movie('The Matrix'))
movies.append(Movie('Inception'))
movies.append(Movie('Interstellar'))
movies.append(Movie('Avatar'))

for movie in movies:
    print(movie.title)



# Program 15

# Exercise 1
class MiniBook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def show(self):
        print('Title:', self.title)
        print('Author:', self.author)
        print('Pages:', self.pages)

book1 = MiniBook('1984', 'George Orwell', 328)
book2 = MiniBook('Brave New World', 'Aldous Huxley', 268)

books = [book1, book2]

for book in books:
    book.show()

# Exercise 2
class MiniCar:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def show(self):
        print('Brand:', self.brand)
        print('Model:', self.model)
        print('Year:', self.year)

car1 = MiniCar('Honda', 'Civic', 2020)
car2 = MiniCar('Toyota', 'Camry', 2021)
car3 = MiniCar('Ford', 'Mustang', 2022)
car4 = MiniCar('Tesla', 'Model 3', 2023)
car5 = MiniCar('Chevy', 'Corvette', 2024)

cars = [car1, car2, car3, car4, car5]

for car in cars:
    car.show()


