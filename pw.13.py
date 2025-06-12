# Simple Exception Handling Example
n = 10
try:
    res = n / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Can't be divided by zero!")

def dividefunction(x, y):
    try:
        z = x/y
    except TypeError:
        print("Type Error: Cannot divide number by string")
    except ZeroDivisionError:
        print("Zero Division Error: Cannot divide by zero")
    except:
        print("Unknown Error")
    else:
        print(z)
    finally:
        print("End of the program")

dividefunction(10, 0)
dividefunction(10, "hello")

def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)

