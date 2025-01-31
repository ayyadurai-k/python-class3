


class Father:
    def display_father(self):
        print("Yes , from father")


class Son(Father):
    def display_son(self):
        print("Yes , from son")


class Daughter(Father):
    def display_daughter(self):
        print("Yes , from daughter")
        

son1 = Son()
son1.display_father()
son1.display_son()

daughter1 = Daughter()
daughter1.display_father()
daughter1.display_daughter()