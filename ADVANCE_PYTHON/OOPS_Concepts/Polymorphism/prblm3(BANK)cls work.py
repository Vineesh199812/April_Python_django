#bank

#account creation [name,account_number,minimum_balance]
#withdraw [amount, current bal]
#deposit [amount, current bal]

class Bank:
    bankname="state bank"
    def acc(self,name,accountno):
        self.name=name
        self.accountno=accountno
        self.min=3000
        self.balance=self.min
        print("welcome",self.name,"your account number is",self.accountno)
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print("your",Bank.bankname,"account has been credited by",self.amount)
        print("your",Bank.bankname,"account balance is",self.balance)
    def withdraw(self,amount1):
        self.amount1=amount1
        if self.amount1>self.balance:
            print("insufficient balance")
        else:
            self.balance=self.balance-self.amount1
            print("your",Bank.bankname,"account debited by",self.amount1)
            print("your current",Bank.bankname,"account balance is",self.balance)

ob=Bank()
ob.acc("vishnu",854525456)
ob.deposit(4000)
ob.withdraw(1000)