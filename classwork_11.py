# 1.Create a class named Movie with attributes
# moviename,year,language,director,rating
# and methods display_details() and update_rating()
class Movie:
    def __init__(self):
        self.movie_name=input('Enter the movie name')
        self.year=input('Enter the year')
        self.language=input('Enter the language')
        self.director=input('Enter the director')
        self.rating=input('Enter the rating')
    def display_details(self):
        print(self.movie_name)
        print(self.year)
        print(self.language)
        print(self.director)
        print(self.rating)
    def updated_rating(self):
        self.rating=input('Enter the rating')
        self.display_details()

m=Movie()
m.display_details()
m.updated_rating()
# 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
#
# Create a parent class Vehicle with the attributes brand, model, color, and year.
# Add a method display() in the Vehicle class to display these details.
# Create two child classes:
# Car with an additional attribute mileage
# Bike with an additional attribute cc
# Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# Create objects of both classes, accept input from the user, and display the details.
# class Vehicle:
#     def __init__(self):
#         self.brand=input('Enter the brand ')
#         self.model=input('Enter the model')
#         self.color=input('Enter the color')
#         self.year=input('Enter the year')
#     def display(self):
#         print('Brand:',self.brand)
#         print('Model:',self.model)
#         print('Color:',self.color)
#         print('Year:',self.year)
# class Car(Vehicle):
#     def __init__(self):
#         Vehicle().__init__()
#         self.milage=input('Enter the milage')
#     def display(self):
#         print('Milage:',self.milage)
# class Bike(Vehicle):
#     def __init__(self):
#         Vehicle().__init__()
#         self.cc=input('Enter the CC of the car')
#     def display(self):
#         print('CC is:',self.cc)
#
# c=Car()
# c.display()
# b=Bike()
# b.display()
