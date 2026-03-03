# Topic 8: Professional File Handling

Handling files is like using a **Storage Locker**. You need to know how to open it, put things in, take things out, and most importantly, remember to lock it when you're done!

---

## 1. The Analogy: The Storage Locker
Before you interact with a file, you must choose a "Mode" (What do you want to do?).

- **`r` (Read):** You open the locker just to **look** at what's inside. You can't change anything.
- **`w` (Write):** You **empty** the locker completely and put new things in. If the locker didn't exist, you build a new one.
- **`a` (Append):** You open the locker and **add** more things to the back without touching what's already there.
- **`+` (Plus):** This turns the locker into a multi-purpose one (Read AND Write).

### 📋 File Mode Cheat Sheet
| Mode | Action | Danger Level |
| :--- | :--- | :--- |
| `r` | Reading only | Safe |
| `w` | Overwriting (Deletes old data) | ⚠️ High |
| `a` | Adding to the end | Safe |
| `rb`/`wb` | Binary (Images/PDFs) | Specialized |

---

## 2. The "Self-Locking" Door: `with open()`
In the old days, programmers had to remember to call `file.close()`. If they forgot, the computer would run out of memory.

**Modern Solution:** Use the `with` keyword. It acts like a door that automatically locks itself the moment you step away.

```python
# The Expert Way
with open("notes.txt", "w") as my_file:
    my_file.write("Don't forget to buy milk!")

# No need to close! Python does it for you.
```

---

## 3. Reading Techniques
1. **The Whole Book (`read()`):** Reads everything at once. Great for small files, but bad for huge ones.
2. **One Line at a Time (`readline()`):** Like reading a book one sentence at a time.
3. **The List (`readlines()`):** Puts every line into a Python list.

---

## 4. Working with JSON (Web Data)
Most modern applications use **JSON** to store data. It looks exactly like a Python dictionary!

```python
import json

user_data = {"name": "Sriram", "points": 100}

# Save (Dump) to file
with open("user.json", "w") as f:
    json.dump(user_data, f)

# Load from file
with open("user.json", "r") as f:
    loaded_data = json.load(f)
```

---

## 💡 Expert Best Practices
- **`encoding="utf-8"`**: Always use this when opening files to avoid "weird characters" on different computers.
- **Check Paths:** Use `os.path.exists()` to check if a file is there before trying to read it.
- **Don't Overwrite by Mistake:** Be very careful with the `"w"` mode!

---

### 📝 Exercise
1. Create a file named `my_story.txt` and write "Once upon a time..." in it using Python.
2. Use the `"a"` mode to add "The End." to the next line.
3. Use a `for` loop to read the file and print each line separately.
