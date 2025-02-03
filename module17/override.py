


class Father:
    def display_city(self):
        print("Chennai")
        
    def display_amount(self):
        print("10K rupees")

class Son(Father):
    
    def display_city(self):
        print("Bangalore")
        

son1 = Son()
son1.display_city()
son1.display_amount()