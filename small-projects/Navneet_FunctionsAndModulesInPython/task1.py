## factorial of a number
def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)

## input from user
num = input("Enter a number: ")

result = factorial(int(num))
print(f"Factorial of {num} is: {result}")


