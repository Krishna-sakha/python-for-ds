# 🐍✨ Python Operators & Type Casting 
# 🌟 Always Remember 🌟
# If you don’t understand anything at first, it’s completely okay!
# Feel free to Google it or watch a small YouTube tutorial on that specific topic.
# Just don’t get stuck in "tutorial hell" — the goal is to learn and keep moving forward.
# We’re here to grow step by step, and our real competition is only with our *past self* 💪

# -- Let's begin with Operators and Type Casting in the simplest way possible --

# --- Arithmetic Operators ---
# Used to perform basic math like +, -, *, /

a = 10
b = 3
print("Addition:", a + b)       # ➕ 10 + 3 = 13
print("Subtraction:", a - b)    # ➖ 10 - 3 = 7
print("Multiplication:", a * b) # ✖️ 10 * 3 = 30
print("Division:", a / b)       # ➗ 10 / 3 = 3.33
print("Floor Division:", a // b)# 🔽 10 // 3 = 3 (no decimal)
print("Modulus:", a % b)        # 🧮 10 % 3 = 1 (remainder)
print("Power:", a ** b)         # 10^3 = 1000

# --- Comparison Operators ---
# These return True/False based on condition

print(a > b)  # True
print(a < b)  # False
print(a == b) # False
print(a != b) # True

# --- Logical Operators ---
# Used to combine conditions

x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# --- Bitwise Operators ---
# Works on binary numbers (0s and 1s)

'''
Cup & Chocolate 🍫 Example:
Imagine binary bits like small cups (🧁🧁🧁🧁).
If a cup has chocolate (1), it's full. If not (0), it's empty.
Bitwise operators just mix the chocolates from 2 sets.
'''
print(5 & 3)    # 0101 & 0011 = 0001 => 1
print(5 | 3)    # 0101 | 0011 = 0111 => 7
print(5 ^ 3)    # 0101 ^ 0011 = 0110 => 6
print(~5)       # ~0101 => -(0101 + 1) = -6

# --- Assignment Operators ---
# Assign values using =, +=, -= etc.

c = 5
c += 3  # c = c + 3 => 8
c *= 2  # c = c * 2 => 16
print(c)

# --- Membership Operators ---
# Check if a value exists in a list or string

my_list = [1, 2, 3]
print(2 in my_list)      # True
print(4 not in my_list)  # True

# --- Identity Operators ---
# Check if 2 variables are the same (same memory location)

x = [1, 2]
y = [1, 2]
z = x
print(x is y)  # False
print(x is z)  # True

# --- Type Casting (Type Conversion) ---
# Converting one data type to another like string to int

# 🍭 Example: string ➡️ int
a = "2"
b = 4
print(int(a) + b)  # int("2") = 2 => 2 + 4 = 6

# 🍬 int ➡️ string
a = 5
c = str(a)
print(c, type(c))  # Output: "5" <class 'str'>

# float ➡️ int (cuts decimals)
pi = 3.14
print(int(pi))  # 3

# int ➡️ float
age = 21
print(float(age))  # 21.0
