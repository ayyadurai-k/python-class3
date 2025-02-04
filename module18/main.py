

class BankAccount:
    def calculate_interest(self,amount):
        print("BA Interest  : ",amount*0.03)

class SavingsAccount(BankAccount):
    def calculate_interest(self, amount):
        print("SA Interest  : ",amount*0.05)

class FixedDepositAccount(SavingsAccount):
    def calculate_interest(self, amount):
        print("FD Interest  : ",amount*0.07)

fd = FixedDepositAccount()
fd.calculate_interest(10000)

sa = SavingsAccount()
sa.calculate_interest(10000)

ba = BankAccount()
ba.calculate_interest(10000)