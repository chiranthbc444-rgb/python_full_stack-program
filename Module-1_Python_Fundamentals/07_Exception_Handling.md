# Topic 7: Professional Exception Handling

In programming, things don't always go as planned. A file might be missing, or a user might enter text when you asked for a number. **Exception Handling** is the art of catching these "accidents" before they crash your program.

---

## 1. The Analogy: Buying a Movie Ticket
Think of an exception block like a trip to the cinema:

- **`try`**: You try to buy a ticket.
- **`except`**: **"The Error"**. The tickets are sold out! You handle this by choosing a different movie instead of crying and staying home (the program crashing).
- **`else`**: **"Success"**. You got the ticket! Now you go and buy popcorn.
- **`finally`**: **"Cleanup"**. Regardless of whether you got a ticket or not, you eventually leave the cinema building.

### 🏗️ The Full Block Syntax
```python
try:
    # 1. Critical code
    age = int(input("Enter your age: "))
    result = 100 / age
except ValueError:
    # 2. Handles specific error (e.g., user typed "abc")
    print("Error: Please enter a valid number!")
except ZeroDivisionError:
    # 2. Handles division by zero
    print("Error: Age cannot be zero!")
else:
    # 3. Runs ONLY if NO errors happened
    print(f"Calculation successful! Result: {result}")
finally:
    # 4. ALWAYS runs no matter what
    print("Thank you for using our calculator.")
```

---

## 2. Raising Your Own Errors
Sometimes, code isn't "broken," but it's "wrong" for your rules. You can use `raise` to stop the program manually.

```python
balance = 50
withdraw = 100

if withdraw > balance:
    raise ValueError("You don't have enough money!")
```

---

## 3. Custom Exceptions (Expert Level)
For professional code, you can create your own specialized error names. This makes your code much easier to read for other developers.

```python
class AgeTooSmallError(Exception):
    """Exception raised for adults-only content."""
    pass

def enter_club(age):
    if age < 18:
        raise AgeTooSmallError("Access Denied: You must be 18+")
    print("Welcome to the club!")

try:
    enter_club(15)
except AgeTooSmallError as e:
    print(e)
```

---

## 💡 Expert Best Practices
1. **Be Specific:** Catch `FileNotFoundError` instead of a generic `Exception`. It’s like knowing exactly why the car won't start (Empty tank vs. Dead battery).
2. **Don't Hide Errors:** Using `except: pass` is like ignoring a "Low Engine Oil" light. It will cause a bigger disaster later!
3. **Clean Up:** Use `finally` to close files or database connections so your computer doesn't run out of memory.

---

### 📝 Exercise
Write a program that asks the user for two numbers and divides them.
- Use `try-except` to handle if they type non-numbers.
- Use `try-except` to handle if they divide by zero.
- Use `finally` to print "Math operation finished."
