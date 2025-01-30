class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department


employee1 = Employee("John", "IT")
employee2 = Employee("Jebisha", "CS")
employee3 = Employee("Eva", "Sales")
employee4 = Employee("Sara", "Mech")

print("Employee 1 name : ",employee1.name)
print("Employee 1 department : ",employee1.department)

print("Employee 2 name : ",employee2.name)
print("Employee 2 department : ",employee2.department)

print("Employee 3 name : ",employee3.name)
print("Employee 3 department : ",employee3.department)

print("Employee 4 name : ",employee4.name)
print("Employee 4 department : ",employee4.department)