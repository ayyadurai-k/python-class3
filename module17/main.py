class People:
    def __init__(self, name, age): # CONSTRUCTOR
        self.name = name
        self.age = age

    def display_people_details(self):
        print("name : ", self.name)
        print("age : ", self.age)


class Student(People):
    def __init__(self, name, age, reg_no, mark):
        self.reg_no = reg_no
        self.mark = mark
        super().__init__(name, age)

    def display_student_details(self):
        print("regno : ", self.reg_no)
        print("mark : ", self.mark)


student1 = Student("Jebisha", 19, 100, 97)

student1.display_people_details()
student1.display_student_details()
