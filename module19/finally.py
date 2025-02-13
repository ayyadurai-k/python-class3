

a = 10
b = 2

try:
    c = a/b
    print("Ans : ",c)
except ZeroDivisionError:
    print("Error : Division by zero is not allowed")
except Exception:
    print("Unknown error")
finally:
    print("This will run every time")