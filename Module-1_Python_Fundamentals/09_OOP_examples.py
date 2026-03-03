"""
Topic 9: Object-Oriented Programming (OOP) Examples
Description: Clear examples illustrating the 4 pillars of OOP.
"""

# --- Example 1: Class, Object, and Encapsulation ---
print("--- Example 1: Encapsulation (Bank Account) ---")
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # Private attribute (Double underscore)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")

    def get_balance(self):
        return self.__balance # Public method to see private data

account = BankAccount("Sriram", 1000)
account.deposit(500)
print(f"Current Balance for {account.owner}: {account.get_balance()}")
# print(account.__balance) # This would fail! It's private.


# --- Example 2: Inheritance & Super() ---
print("\n--- Example 2: Inheritance (Vehicles) ---")
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"The {self.brand} is starting...")

class ElectricCar(Vehicle): # Inherits from Vehicle
    def __init__(self, brand, battery_size):
        super().__init__(brand) # Calls the Parent's __init__
        self.battery_size = battery_size

    def show_specs(self):
        print(f"Brand: {self.brand}, Battery: {self.battery_size}kWh")

my_tesla = ElectricCar("Tesla", 100)
my_tesla.start()
my_tesla.show_specs()


# --- Example 3: Polymorphism ---
print("\n--- Example 3: Polymorphism (Animal Sounds) ---")
class Animal:
    def speak(self):
        pass # To be defined by children

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat(), Dog()]
for a in animals:
    print(a.speak()) # Same command, different results!


# --- Example 4: Abstraction (The Template) ---
print("\n--- Example 4: Abstraction (Remote Control) ---")
from abc import ABC, abstractmethod

class RemoteControl(ABC): # This class cannot be instantiated!
    @abstractmethod
    def toggle_power(self):
        """Every remote MUST have a power button."""
        pass

class TVRemote(RemoteControl):
    def toggle_power(self):
        print("TV Power Toggled: Screen is now ON.")

class FanRemote(RemoteControl):
    def toggle_power(self):
        print("Fan Power Toggled: Blades are now SPINNING.")

# my_remote = RemoteControl() # This would throw an error!
tv = TVRemote()
tv.toggle_power()

fan = FanRemote()
fan.toggle_power()


# --- Example 5: Magic Methods (__str__) ---
print("\n--- Example 5: Magic Methods (__str__) ---")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' written by {self.author}"

my_book = Book("Python Mastery", "Expert")
print(my_book) # Uses the __str__ method automatically
