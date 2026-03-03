"""
Topic 7: Exception Handling Examples
Description: Concrete, runnable examples covering all possible exception handling scenarios.
"""

# --- Example 1: The Basic Try-Except ---
print("--- Example 1: Basic Handling ---")
try:
    number = int("abc")  # This will fail
except ValueError:
    print("Caught an error: You can't turn letters into numbers!")

# --- Example 2: The Full Block (Try-Except-Else-Finally) ---
print("\n--- Example 2: The Full Block ---")
def divide_numbers(a, b):
    try:
        print(f"Attempting: {a} / {b}")
        result = a / b
    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")
    else:
        print(f"Success! The result is {result}")
    finally:
        print("Cleaning up... operation finished.")

divide_numbers(10, 2)  # Normal case
divide_numbers(10, 0)  # Error case

# --- Example 3: Multiple Exception Types ---
print("\n--- Example 3: Multiple Exceptions ---")
try:
    # my_list = [1, 2]
    # print(my_list[5]) # Uncomment to trigger IndexError
    x = 10 / 0         # Triggers ZeroDivisionError
except IndexError:
    print("Error: That index doesn't exist in the list.")
except ZeroDivisionError:
    print("Error: Don't divide by zero.")
except Exception as e:
    print(f"Caught a general error: {e}")

# --- Example 4: Custom Exceptions ---
print("\n--- Example 4: Custom Exceptions ---")

class CoffeeTooHotError(Exception):
    """Raised when the coffee is dangerously hot."""
    pass

def drink_coffee(temp):
    if temp > 80:
        raise CoffeeTooHotError(f"Ouch! {temp}C is way too hot!")
    print(f"Ahhh, {temp}C is just right.")

try:
    drink_coffee(95)
except CoffeeTooHotError as e:
    print(f"Safety Warning: {e}")

# --- Example 5: Raising Exceptions ---
print("\n--- Example 5: Manual Raising ---")
age = -5
try:
    if age < 0:
        raise ValueError("Age cannot be a negative number!")
except ValueError as error:
    print(f"Validation Error: {error}")
