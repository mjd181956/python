"""
银行账户私有化案例
"""

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):  # 存款
        self.__balance += amount

    def withdraw(self, amount):  # 取款
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__pay_interst()
            return amount
        else:
            print("余额不足")
            return 0

    def __pay_interst(self):
        self.__balance -= 5

    def get_balance(self):
        return self.__balance


account = BankAccount("123456", 1000)
account.deposit(500)

print(account.withdraw(600))

# print(account.__balance)  # 私有，外部不能使用
print(account.get_balance())
