class BankAccount:
    def __init__(self, balance, intrest_rate ):
        self.balance = balance
        self.intrest_rate = intrest_rate
        self.amount = 0

    def deposite(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print(f"Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.intrest_rate
        return self

sajeda_account = BankAccount(2000, 0.2)
shatha_account = BankAccount(10000, 0.2)

sajeda_account.deposite(100).deposite(200).deposite(400).withdrawal(2800).yield_interest().display_account_info()
shatha_account.deposite(5000).deposite(400).withdrawal(700).withdrawal(100).withdrawal(30).withdrawal(1000).yield_interest().display_account_info()
