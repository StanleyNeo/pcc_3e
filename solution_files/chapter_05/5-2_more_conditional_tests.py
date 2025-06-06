# 20250606 more condition test
# Tests for equality and inequality with strings
print("\n--- String Equality/Inequality Tests ---")
city = 'New York'
print("Is city == 'New York'? I predict True.")  # True
print(city == 'New York')
print("Is city != 'Boston'? I predict True.")    # True
print(city != 'Boston')
print("Is city == 'Los Angeles'? I predict False.")  # False
print(city == 'Los Angeles')
print("Is city != 'New York'? I predict False.")     # False
print(city != 'New York')

# Tests using the lower() method
print("\n--- Case Insensitive Tests with lower() ---")
language = 'Python'
print("Is language.lower() == 'python'? I predict True.")  # True
print(language.lower() == 'python')
print("Is language.lower() == 'java'? I predict False.")   # False
print(language.lower() == 'java')

# Numerical tests
print("\n--- Numerical Tests ---")
number = 42
print("Is number == 42? I predict True.")              # True (equality)
print(number == 42)
print("Is number != 24? I predict True.")              # True (inequality)
print(number != 24)
print("Is number > 30? I predict True.")               # True (greater than)
print(number > 30)
print("Is number < 50? I predict True.")               # True (less than)
print(number < 50)
print("Is number >= 42? I predict True.")              # True (greater than or equal)
print(number >= 42)
print("Is number <= 42? I predict True.")              # True (less than or equal)
print(number <= 42)
print("Is number == 24? I predict False.")             # False (equality)
print(number == 24)
print("Is number != 42? I predict False.")             # False (inequality)
print(number != 42)
print("Is number > 50? I predict False.")              # False (greater than)
print(number > 50)
print("Is number < 30? I predict False.")              # False (less than)
print(number < 30)
print("Is number >= 50? I predict False.")             # False (greater than or equal)
print(number >= 50)
print("Is number <= 30? I predict False.")             # False (less than or equal)
print(number <= 30)

# Tests using 'and' and 'or' keywords
print("\n--- Logical Operator Tests ---")
age = 25
height = 68  # inches
print("Is age > 20 and height > 60? I predict True.")  # True (and)
print(age > 20 and height > 60)
print("Is age < 18 or height < 60? I predict False.")  # False (or)
print(age < 18 or height < 60)
print("Is age > 30 or height > 70? I predict False.")  # False (or)
print(age > 30 or height > 70)
print("Is age > 20 and height < 60? I predict False.") # False (and)
print(age > 20 and height < 60)

# Test whether an item is in a list
print("\n--- List Membership Tests ---")
fruits = ['apple', 'banana', 'orange']
print("Is 'banana' in fruits? I predict True.")        # True
print('banana' in fruits)
print("Is 'grape' in fruits? I predict False.")        # False
print('grape' in fruits)

# Test whether an item is not in a list
print("\n--- List Non-Membership Tests ---")
colors = ['red', 'green', 'blue']
print("Is 'yellow' not in colors? I predict True.")    # True
print('yellow' not in colors)
print("Is 'red' not in colors? I predict False.")      # False
print('red' not in colors)