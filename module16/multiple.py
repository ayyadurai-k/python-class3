


class Father:
    def display_father(self):
        print("Yes , from father")

class Mother:
    def display_mother(self):
        print("Yes , from mother")


class Daughter(Father,Mother):
    def display_daughter(self):
        print("Yes , from daughter")
        

daughter1 = Daughter()

daughter1.display_father()
daughter1.display_mother()
daughter1.display_daughter()