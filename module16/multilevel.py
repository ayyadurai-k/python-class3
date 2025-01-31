
class GrandFather:
    def display_grandfather(self):
        print("Yes , From GrandFather")

class Father(GrandFather):
    def display_father(self):
        print("Yes , From Father")
        
class Son(Father):
    def display_son(self):
        print("Yes , From Son")


son1 = Son()
son1.display_grandfather()
son1.display_father()
son1.display_son()
        

