"""Some examples of Python sets and frozensets.

A set is a collection of unique items.
It does not keep duplicate values and does not preserve order.
"""

# A set stores unique values. Order is not guaranteed.
fruits = {"apple", "banana", "orange"}
tropical_fruits = {"banana", "mango", "pineapple"}

# union: all items from both sets
print("Union:", fruits | tropical_fruits)
print()
print("Union method:", fruits.union(tropical_fruits))
print()

# intersection: items present in both sets
print("Intersection:", fruits & tropical_fruits)
print()
print("Intersection method:", fruits.intersection(tropical_fruits))
print()

# difference: items in the first set but not in the second set
print("Difference:", fruits - tropical_fruits)
print()

# symmetric difference: items in one set or the other, but not both
print("Symmetric difference:", fruits ^ tropical_fruits)
print()

# subset and superset checks
favorites = {"apple", "banana"}
print("Is favorites a subset of fruits?", favorites <= fruits)
print()
print("Is favorites a proper subset of fruits?", favorites < fruits)
print()
print("Is fruits a superset of favorites?", fruits >= favorites)
print()

# disjoint: no common elements
print("Are fruits and {'kiwi'} disjoint?", {"kiwi"}.isdisjoint(fruits))
print()

# Sets are mutable: we can add, remove, or update values.
numbers = {1, 2}
numbers.add(3)          # adds 3
numbers.discard(99)     # safe even if 99 is not in the set
numbers.update({3, 4})  # adds new items
print("Updated numbers:", numbers)
print()
print("Does numbers contain 2?", 2 in numbers)
print()

# A frozenset is like a set, but it cannot be changed after creation.
colors = frozenset({"red", "green"})
extra_colors = frozenset({"green", "blue"})
print("Frozen set union:", colors | extra_colors)
print()
print("Is {'red'} a subset of colors?", frozenset({"red"}) <= colors)
print()

# A frozenset is hashable, so it can be used as a dictionary key.
color_labels = {colors: "traffic-light colors"}
print("Dictionary using frozenset key:", color_labels[colors])
print()

# Output examples for each operation
print("Final fruits set:", fruits)
print()
print("Final tropical fruits set:", tropical_fruits)
print()
print("Final numbers set:", numbers)
print()
print("Final colors set:", colors)
print()

