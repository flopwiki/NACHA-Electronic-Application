class Account:
    def __init__(self, acc_id, acc_bal=0.0):
        
        self.acc_id = acc_id
        self.acc_bal = acc_bal



    def check_balance(self):
        return self.acc_bal

    def deposit(self, amount):
        self.acc_bal += amount


    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.acc_bal -= amount
