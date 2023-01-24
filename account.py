from customer import Customer
class Account:
    def __init__(self, owner, amount = 0):
        if type(owner) != Customer:
            raise AttributeError
        self.owner = owner
        self.amount = amount

    def deposit(self, dep_amount):
        if type(dep_amount) != int and type(dep_amount) != float:
            raise TypeError("Invalid Data Type. Please enter a number")
        if dep_amount < 0:
            raise AttributeError("Amount cannot be negative.")
        self.amount += dep_amount

    def withdraw(self, withdraw_amount):
        if type(withdraw_amount) != int and type(withdraw_amount) != float:
            raise TypeError("Invalid Data Type. Please enter a number")
        if withdraw_amount < 0:
            raise AttributeError("Amount cannot be negative.")
        self.amount -= withdraw_amount

    def transfer(self, account, trans_amount):
        if not isinstance(account, Account):
            raise TypeError("Not a valid account")
        self.amount -= trans_amount
        account.amount += trans_amount

class CreditAccount(Account):
    def __init__(self, owner, interest, amount = 0):
        super().__init__(owner, amount)
        if not interest in range(0, 100):
            raise ValueError("invalid interest")
        self.interest = interest

    def compute_interest(self):
        if self.amount < 0:
            self.amount = self.amount * (100 + self.interest) / 100
            self.amount -= 10

class SavingsAccount(Account):
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        if value < 0:
            raise UserWarning
        self._amount = value
