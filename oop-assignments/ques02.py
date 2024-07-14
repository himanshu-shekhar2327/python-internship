class BankAccount :
    
    def __init__(self,account_holder,account_number,balance) :
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance

    def deposit(self, amount):
        
        
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}. New balance is {self.balance}.")
    
    
    def withdraw(self, amount):
       
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from account number {self.account_number}. New balance is {self.balance}.")
    
    
    def get_balance(self):
        
        return self.balance

acc_holder = input("Enter the account holder name :")
acc_no =  input("Enter the account number : ")
account1=BankAccount(acc_holder, acc_no,10000.0)
print(f"Account holder: {account1.account_number} \n Account number: {account1.account_holder} \n Balance: {account1.get_balance()}")
inp_deposit_money = int(input("Enter the deposit money :"))
account1.deposit(inp_deposit_money)
inp_withdraw_money = int(input("Enter the withdraw money :"))
account1.withdraw(inp_withdraw_money)
print(f"Current balance: {account1.get_balance()}")