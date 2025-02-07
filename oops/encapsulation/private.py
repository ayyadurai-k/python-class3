
class BankAccount:
    def __init__(self,amount):
        self.__amount = amount
    
    def get_amount(self):
        return self.__amount
    
    def set_amount(self,amount):
        if amount > 500:
            self.__amount = self.__amount + amount
            print("Amount added successfully")
        else :
            print("Invalid amount")

class SubBankAccount(BankAccount):
    def get_amount(self):
        return self.__amount
    

ba = BankAccount(10000)
print("Amount before added : ",ba.get_amount())
ba.set_amount(0)
ba.set_amount(3000)
print("Amount after added  : ",ba.get_amount())

sba = SubBankAccount()
print("Amount before added sba : ",sba.get_amount())