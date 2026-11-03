def factorial(number):
	if number <= 1:
		return 1
	return number * factorial(number - 1)


number = int(input("Enter a number: "))

if number < 0:
	print("Invalid number.")
else:
	print(f"Factorial of {number} is {factorial(number)}")
