import math

def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(x)

def factorial(n):
    if n < 0:
        raise ValueError("Cannot compute factorial of a negative number")
    return math.factorial(n)

def power(x, b):
    return x ** b

def natural_log(x):
    if x <= 0:
        raise ValueError("Cannot compute natural logarithm of non-positive number")
    return math.log(x)

def main():
    options = {
        1: ("Square Root (√x)", square_root),
        2: ("Factorial (x!)", factorial),
        3: ("Natural Logarithm (ln(x))", natural_log),
        4: ("Power Function (x^b)", power)
    }

    print("Options:")
    for key, (description, _) in options.items():
        print(f"{key}. {description}")

    try:
        option = int(input("Enter your option: "))
        if option not in options:
            raise ValueError("Invalid option")

        value = float(input("Enter the value: "))
        if option == 4:
            exponent = float(input("Enter the exponent: "))
            result = options[option][1](value, exponent)
        else:
            result = options[option][1](value)

        print(f"Result: {result}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
