alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
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