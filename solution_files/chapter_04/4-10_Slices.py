#4-10 Slices
# Create a list of multiples of 3 from 3 to 30
multiples_of_three = list(range(3, 31, 3))

# Print the original list
print("Original list of multiples of 3:")
print(multiples_of_three)

# Print the first three items [:3]
print("\nThe first three items in the list are:")
print(multiples_of_three[:3])

# Print three items from the middle [middle_start:middle_start + 3]
print("\nThree items from the middle of the list are:")
middle_start = len(multiples_of_three) // 2 - 1
print(multiples_of_three[middle_start:middle_start + 3])

# Print the last three items [-3:]
print("\nThe last three items in the list are:")
print(multiples_of_three[-3:])