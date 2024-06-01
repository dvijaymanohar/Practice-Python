
class BankAccount():
    def __init__(self, account_number: int):
        self.__account_number: int = account_number
        self.__account_balance : float = 0
        self.__transactions : lists[float] = []

    def deposit(self, amount: float) -> None:
        self.__account_balance += amount
        self.__transactions.append(amount)

    def withdraw(self, amount: float) -> bool | str:
        if amount < self.__account_balance:
            self.__account_balance -= amount
            self.__transactions.append(amount)
            return True
        else:
            return "Insufficient balance"

    def get_balance(self):
        return self.__account_balance

    def get_transactions(self) -> list[float]:
        return self.__transactions

def main():
    account = BankAccount(123)
    account.deposit(20.0)

    if account.withdraw(10.0) == True:
        print('Withdrawal successful')

    if account.withdraw(15.0) == 'Insufficient balance':
        print('Insufficient balance\n')

    print(f'transactions: {account.get_transactions()}')

if __name__ == "__main__":
    main()
