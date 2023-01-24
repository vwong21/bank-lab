from account import Customer, Account, CreditAccount, SavingsAccount

class Bank:
    def __init__(self, name):
        self.name = name
        self.list_of_accounts = []

    def create_account(self, category, owner, interest = 0):
        if category != "account" and category != "credit" and category != "savings":
            raise ValueError("Invalid account type")
        if type(owner) != Customer:
            raise AttributeError("Invalid owner")
        if category == "credit":
            if interest == 0:
                raise UserWarning("Please enter an interest rate")
            self.account = CreditAccount(owner, interest)
        elif category == "savings":
            self.account = SavingsAccount(owner)
        elif category == "account":
            self.account = Account(owner)
        else:
            raise AttributeError
        self.list_of_accounts.append(self.account)
        return self.account
    
    def find_accounts_by_ssn(self, ssn):
        if type(ssn) != str:
            raise TypeError("Enter a string")
        self.matching_ssn_accounts = []
        for _ in self.list_of_accounts:
            if ssn == _.owner.ssn:
                self.matching_ssn_accounts.append(_)
        return self.matching_ssn_accounts

    def find_accounts_by_name(self, name):
        self.matching_name_accounts = []
        if type(name) != str:
            raise TypeError("Enter a string")
        for _ in self.list_of_accounts:
            if name in _.owner.name:
                self.matching_name_accounts.append(_)
        return self.matching_name_accounts
    
    @property
    def balance(self):

        return self.balance
    
    @balance.getter
    def balance(self):
        total = 0
        for _ in self.list_of_accounts:
            total += _.amount
        return total