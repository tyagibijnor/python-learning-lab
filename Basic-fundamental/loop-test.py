# Python loops repeat code so you do not have to write it again and again.

# A for loop repeats once for each item in a sequence.
for fruit in ["apple", "banana", "orange"]:
	print(fruit)

# range(start, stop) generates numbers from start up to, but not including, stop.
# This prints 1, 2, 3, 4, and 5.
for number in range(1, 6):
	print("Number:", number)

# range(start, stop, step) adds a step value.
# Start at 2, stop before 11, and jump by 2 each time.
# This prints 2, 4, 6, 8, and 10.
for even_number in range(2, 11, 2):
	print("Even number:", even_number)

# range(len(profits)) gives each valid index in the list.
# List indexes start at 0, so this prints index-profit pairs.
profits = [9, 11, 6, 10]
for index in range(len(profits)):
	print("Index:", index, "Profit:", profits[index])

# A while loop repeats as long as its condition is True.
count = 1
while count <= 3:
	print("Count:", count)
	count += 1  # Increase count so the loop eventually stops.

# Use break to stop a loop early.
for number in range(1, 6):
	if number == 4:
		break
	print("Before break:", number)

# Use continue to skip the current turn and move to the next one.
for number in range(1, 6):
	if number == 3:
		continue
	print("Not skipped:", number)
