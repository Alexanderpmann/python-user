class User:
    def __init__(self,name):
        self.name = name
        self.amount = 0
    # adding the deposit method

    def make_deposit(self,amount):
        self.amount += amount
        return self

    def make_withdrawal(self,amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.amount}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

Waldo = User('Waldo')
Mickey = User('Mickey Mouse')
Minnie = User('Minnie Mouse')

Waldo.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(45).display_user_balance()
Mickey.make_deposit(1000).make_deposit(1000).make_withdrawal(500).make_withdrawal(300).display_user_balance()
Minnie.make_deposit(1500).make_withdrawal(1000).make_withdrawal(5000).make_withdrawal(3000).display_user_balance()
Minnie.transfer_money(500, Mickey)
