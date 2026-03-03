"""
Topic 8: File Handling Examples
Description: Practical examples for reading, writing, and managing files correctly.
"""
import os
import json

# --- Example 1: Writing and Reading a Text File ---
print("--- Example 1: Basic Text Files ---")
filename = "example.txt"

# Step 1: Write to the file (Overwrites if exists)
with open(filename, "w", encoding="utf-8") as f:
    f.write("Line 1: Hello Python!\n")
    f.write("Line 2: File handling is fun.\n")

# Step 2: Read from the file
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()
    print("Full Content read at once:")
    print(content)

# --- Example 2: Appending Data ---
print("\n--- Example 2: Appending Data ---")
with open(filename, "a", encoding="utf-8") as f:
    f.write("Line 3: This was added later using 'a' mode.\n")

# Read line by line (Memory efficient)
print("Reading line by line using a loop:")
with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        print(f" > {line.strip()}")

# --- Example 3: Handling JSON Data ---
print("\n--- Example 3: JSON Data (Dictionaries) ---")
data = {
    "module": "Python Fundamentals",
    "lessons": ["Syntax", "Loops", "Files"],
    "completed": True
}

# Saving JSON
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
print("Data saved to data.json")

# Loading JSON
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print(f"Loaded Module Name: {loaded_data['module']}")

# --- Example 4: Safety Check (Checking if path exists) ---
print("\n--- Example 4: Safety Check ---")
if os.path.exists("non_existent_file.txt"):
    print("Found it!")
else:
    print("Warning: non_existent_file.txt does not exist. Skipping read.")

# Cleanup of example files
# os.remove(filename)
# os.remove("data.json")
