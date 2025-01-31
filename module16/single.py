

class Father:
    def display_father(self):
        print("Yes , from father")
        

class Son(Father):
    def display_son(self):
        print("Yes , from son")
        


son1 = Son()


son1.display_father()
son1.display_son()