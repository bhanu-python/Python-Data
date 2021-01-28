class Account():


    def __init__(self,depos,withd,balance=1000):
        self.withd=withd
        self.depos=depos
        self.balance=balance

    def deposit(self):
        self.balance=self.depos + self.balance
        print("Account has been cedited with : {}".format(self.depos))
        

    def withdraw(self):
        if self.balance < self.withdraw:
            print("Your balance is low !")
        else:
            self.balance=self.balance-self.withd
            print("account has beendebited with : {}".format(self.withd))
    
    def __str__(self):
        return f"Your current account balance is : {self.balance}"

    

account=Account(1000,500)

account.deposit()

print(str(account))
