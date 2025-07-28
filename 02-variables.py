# 02 - Variables and Data Types

# 🧠 What is a Variable?
# A variable is like a jar where we store some value.
# Imagine you have a jar labeled "sugar" and you put 5 spoons of sugar in it.
# Similarly, in Python, we can label a container (called variable) and store data in it.

# 🔸 Example 1: Storing a number in a jar
laddu = 5
print(laddu)  # Output: 5

# 🔸 Example 2: Storing a name
radha = "beautiful"
print(radha)  # Output: beautiful

# 🔸 Example 3: Decimal number
krishna = 3.14
print(krishna)  # Output: 3.14

# 🔄 Variables hold only the latest assigned value
message = "Jai Radhe"
message = "Radha Rani ki Jai"
print(message)  # Output: Radha Rani ki Jai

# 🧂 Just like putting pickle in a jar replaces what was in it before,
# assigning a new value to a variable replaces the old one.

# 🔐 Rules for Naming Variables (Important!)
# - Can start with letters or underscore (_) only
# - Cannot start with a number
# - Cannot contain special characters like @, $, %, etc.
# - Cannot be any of Python’s predefined keywords (like 'if', 'while', 'for')
# - Python is case-sensitive: 'Radha' and 'radha' are different

# ✅ Valid variable names
age = 18
first_name = "Radha"
totalMarks = 90

# ❌ Invalid variable names (these will cause errors)
# 1age = 23         # ❌ starts with number
# total-marks = 90  # ❌ contains '-'
# if = 5            # ❌ 'if' is a keyword

🚫 🔐 Python Keywords (Can’t be used as variable names)
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield


# 📦 Python Data Types (we’ll dive deeper later, just an intro)

# 1. int → Whole numbers (without decimal)
kaju = 10
print(type(kaju))  # Output: <class 'int'>

# 2. float → Decimal numbers
barfi = 2.5
print(type(barfi))  # Output: <class 'float'>

# 3. str → Text (anything inside quotes)
mithai = "sweet"
print(type(mithai))  # Output: <class 'str'>

# 4. bool → True or False only
is_pure = True
print(type(is_pure))  # Output: <class 'bool'>

# 🎉 Don’t worry if you don’t understand everything at once. You’re doing amazing.
# Slowly you’ll become best friends with variables just like Radha and Krishna 💙
