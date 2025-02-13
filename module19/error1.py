

a = 10
b = 5

numbers = [12,13,14,15]

try :
    c = a/b
    print(numbers[10])
    print(" Answer :  ",c)
except ZeroDivisionError:
    print("Divided by zero error , Please check values")
except IndexError:
    print("Provided index not in the list")
except Exception:
    print("Unknown error")

    