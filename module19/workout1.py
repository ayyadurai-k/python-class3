
numbers = [10,11,12,13]

try:
    class Aria:
        def display_aria(self):
            print("Yes, From Aria")
    aria1 = Aria()
    aria1.display_aria()
except NameError:
    print("Error: invalid name")
except AttributeError:
    print("Error: invalid attribute")
except Exception:
    print("Unknown error")
