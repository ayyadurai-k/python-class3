
class Student:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    def print_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
    
    def check_adult(self):
        if self.age >= 18:
            print(self.name, "is an adult")
        else:
            print(self.name, "is not an adult")
        
        
student1 = Student("John", 22)
student2 = Student("Jebisha", 15)

student1.print_details()
student1.check_adult()

student2.print_details()
student2.check_adult()
