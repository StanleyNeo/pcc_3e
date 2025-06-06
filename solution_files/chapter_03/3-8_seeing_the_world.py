locations = ['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']

print("Original order:")
print(locations)

print("\nAlphabetical:")
print(sorted(locations))

print("\nOriginal order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("\nOriginal order:")
print(locations)

print("\nReversed:")
locations.reverse()
print(locations)

print("\nOriginal order:")
locations.reverse()
print(locations)

print("\nAlphabetical")
locations.sort()
print(locations)

print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)


locations = ['jurong', 'clementi', 'sengkang', 'hougang', 'ang mo kio']

# not alphabetical order Original order
print("Original order:")
print(locations)

# sorted() original remain
print("\nAlphabetical: sorted()")
print(sorted(locations))

# show still original
print("\nOriginal order: original remain")
print(locations)

# sorted(locations, reverse=True) set True
print("\nReverse alphabetical: reverse order")
print(sorted(locations, reverse=True))

# show still original
print("\nOriginal order: original remain")
print(locations)

# locations.reverse()
print("\nReversed: using .reverse()")
locations.reverse()
print(locations)

# locations.reverse() do again back to original
print("\nOriginal order: 2nd .reverse()")
locations.reverse()
print(locations)

print("\nAlphabetical .sort()")
locations.sort()
print(locations)

print("\nReverse alphabetical .sort(reverse=True")
locations.sort(reverse=True)
print(locations)