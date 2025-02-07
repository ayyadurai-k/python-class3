

class BankAccount:
    def __init__(self,amount):
        self._amount = amount

class SubBankAccount(BankAccount):
    def __init__(self,amount):
        super().__init__(amount)
    
    def get_amount(self):
        return self._amount


sba = SubBankAccount(10000)


print("Amount : ",sba.get_amount())