"""Examples of common operations with numbers in Python."""

# A list of numbers to use in the examples.
numbers = [12, 5, 28, 3, 17, 5]

print("Numbers:", numbers)

# min() and max() find the smallest and largest values.
print("Smallest number:", min(numbers))
print("Largest number:", max(numbers))

# sorted() returns a new list in ascending order; it does not change numbers.
ascending = sorted(numbers)
print("Sorted from smallest to largest:", ascending)

# Use reverse=True to sort from largest to smallest.
descending = sorted(numbers, reverse=True)
print("Sorted from largest to smallest:", descending)

# The first item in an ascending sorted list is the smallest value.
print("Smallest using sorted():", ascending[0])

# A few other useful number operations.
print("Total:", sum(numbers))
print("Count:", len(numbers))
print("Average:", sum(numbers) / len(numbers))

# sort() changes the original list in place.
numbers.sort()
print("Original list after numbers.sort():", numbers)
