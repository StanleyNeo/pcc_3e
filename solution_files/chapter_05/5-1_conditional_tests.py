# 20250606 5-5 conditional test
#
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Test 1: String equality
fruit = 'apple'
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')

# Test 2: String inequality
print("\nIs fruit != 'orange'? I predict True.")
print(fruit != 'orange')

# Test 3: Number comparison
age = 25
print("\nIs age > 20? I predict True.")
print(age > 20)

# Test 4: List membership
colors = ['red', 'green', 'blue']
print("\nIs 'green' in colors? I predict True.")
print('green' in colors)

# Test 5: Boolean check
is_sunny = True
print("\nIs it sunny? I predict True.")
print(is_sunny)

# Test 6: Case sensitivity check
name = 'John'
print("\nIs name == 'john'? I predict False (case sensitive).")
print(name == 'john')

# Test 7: Number comparison
print("\nIs age < 18? I predict False.")
print(age < 18)

# Test 8: List non-membership
print("\nIs 'yellow' in colors? I predict False.")
print('yellow' in colors)

# Test 9: Multiple conditions
temperature = 75
print("\nIs temperature > 100 or < 50? I predict False.")
print(temperature > 100 or temperature < 50)

# Test 10: Boolean negation
print("\nIs it not sunny? I predict False.")
print(not is_sunny)