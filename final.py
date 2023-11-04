import random

class Admin:
    def __init__(self):
        self.accounts={}
        self.allow_loans=True

    def create_account(self,name,email,address,account_type):
        account = User(name,email,address,account_type)
        self.accounts[account.account_number]=account
        return account
    
    def delete_account(self,account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} deleted")
        else:
            print(f"Account {account_number} not found")
    
    def list_accounts(self):
        for account_number,account  in self.accounts.items():
            print(account_number, account.name)

    def total_balance(self):
        total=0
        for account in self.accounts.values():
            total+=account.balance
        return total
    
    def total_loan_amount(self):
        total=0
        for account in self.accounts.values():
            total+=account.loan_amount
        return total
    
    def total_loans(self):
        total=0
        for account in self.accounts.values():
            total += account.num_loans
        return total
    
        
    def print_accounts(self):
        print(f"Total accounts: {len(self.accounts)}")
        print(f"Total balance: {self.total_balance()}")
        print(f"Total loans: {self.total_loans()}")

    def is_loan_available(self):
        self.allow_loans = not self.allow_loans
        print("Loan featured status changed")
        print("--------------------------")

    def print_all_users(self):
        for account in self.accounts.values():
            print(f"Account Number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Email: {account.email}")
            print(f"Address: {account.address}")
            print(f"Account Type: {account.account_type}")
            print(f"Balance: {account.balance}")
            print(f"Number of Loans: {account.num_loans}")
            print(f"Allow Loans: {'Yes' if banking_system.allow_loans else 'No'}")
            print("--------------------------")

class User:
    def __init__(self,name,email,address,account_type):
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.balance=0
        self.account_number = random.randint(100000,999999)
        self.transaction_history=[]
        self.num_loans=0
        self.loan_amount=0

    def deposit(self,amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        print("**** Deposit successful ****")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Withdraw amount exceeded")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw {amount}")
            print("**** Withdraw successful ****")
        
    def take_loan(self, amount):
        if banking_system.allow_loans and self.num_loans < 2:
            self.balance += amount
            self.num_loans += 1
            self.loan_amount+=amount
            self.transaction_history.append(f"Took loan of {amount}")
            print("**** Loan request accepted ****")
        elif not self.allow_loans:
            print("Loans are not allow for this account")
        else:
            print("Can only take 2 loans")

    def transfer(self,receiver,amount):
        if receiver.account_number not in banking_system.accounts:
                print("Account does not exists")
        else:
            if amount > self.balance:
                print("Insufficient balance")
            else:
                self.balance -= amount
                receiver.balance += amount
                self.transaction_history.append(f"Transferred {amount} to account {receiver.account_number}")
                receiver.transaction_history.append(f"Received {amount} from account {self.account_number}")
                print("**** Transfer successful ****")

    def print_statement(self):
        print(f"Name: {self.name}") 
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

banking_system = Admin()

print("1.CREATE AN ACCOUNT")
print("2.DEPOSIT")
print("3.WITHDRAW")
print("4.CHECK BALANCE")
print("5.TRANSACTION HISTORY")
print("6.APPLY FOR LOAN")
print("7.BALANCE TRANSFER")
print("8.Admin")
print("0.Exit")
print("--------------------------")

choice=int(input("Enter your choice:"))

while(choice!=0):
    if (choice==1):
        name=input("Enter name:")
        email=input('Enter your email:')
        address=input("Enter your address:")
        account_type=input("Account type:")
        user = banking_system.create_account(name,email,address,account_type)
        print(f"Here is your account number:{user.account_number}")
        print("--------------------------")
    elif(choice==2):
        account_number=int(input("Enter account number you want to deposit:"))
        deposit_amount=int(input('Enter amount to deposit:'))
        if account_number in banking_system.accounts:
            account=banking_system.accounts[account_number]
            account.deposit(deposit_amount)
            print("--------------------------")
        else:
            print("Account not found")
            print("--------------------------")
    elif choice == 3:
        account_number = int(input("Enter account number you want to withdraw from:"))
        withdraw_amount = int(input('Enter amount to withdraw:'))
        if account_number in banking_system.accounts:
            account = banking_system.accounts[account_number]
            account.withdraw(withdraw_amount)
            print("--------------------------")
        else:
            print("Account not found")
            print("--------------------------")
    elif(choice==4):
        account_number = int(input("Enter account number you want to check balance for:"))
        if account_number in banking_system.accounts:
            account = banking_system.accounts[account_number]
            print(f"Balance: ${account.balance}")
            print("--------------------------")
        else:
            print("Account not found")
            print("--------------------------")

    elif choice == 5:
        account_number = int(input("Enter account number to view transaction history:"))
        if account_number in banking_system.accounts:
            account = banking_system.accounts[account_number]
            account.print_statement()
            print("--------------------------")
        else:
            print("Account not found")
            print("--------------------------")
            
    elif choice == 6:
        account_number = int(input("Enter account number to apply for a loan:"))
        loan_amount = int(input('Enter the loan amount:'))
        if account_number in banking_system.accounts:
            account = banking_system.accounts[account_number]
            account.take_loan(loan_amount)
            print("--------------------------")
        else:
            print("Account not found")
            print("--------------------------")
    elif choice == 7:
        sender_account_number = int(input("Enter your account number:"))
        receiver_account_number = int(input("Enter the receiver account number:"))
        transfer_amount = int(input('Enter the amount to transfer:'))
        if sender_account_number in banking_system.accounts and receiver_account_number in banking_system.accounts:
            sender = banking_system.accounts[sender_account_number]
            receiver = banking_system.accounts[receiver_account_number]
            sender.transfer(receiver, transfer_amount)
            print("--------------------------")
        else:
            print("Account not found")
            print("--------------------------")
    
    elif choice == 8:
        password = input("Enter password:")
        # Admin panel password
        default_pass="1A2bB345"

        if(password == default_pass):
            print("1.CREATE AN ACCOUNT")
            print("2.DELETE AN ACCOUNT")
            print("3.ACCOUNTS LIST")
            print("4.CHECK TOTAL BALANCE OF THE BANK")
            print("5.CHECK TOTAL LOAN AMOUNT")
            print("6.LOAN FEATURE OF THE BANK")
            print("0.EXIT")
            print("--------------------------")

            choice = int(input("Enter your choice:"))

            while(choice!=0):
                if(choice==1):
                    name=input("Enter name:")
                    email=input('Enter your email:')
                    address=input("Enter your address:")
                    account_type=input("Account type:")
                    user = banking_system.create_account(name,email,address,account_type)
                    print(f"Here is your account number:{user.account_number}")
                    print("--------------------------")
                elif(choice==2):
                    account_number=int(input("Enter account number to DELETE:"))
                    if account_number in banking_system.accounts:
                        banking_system.delete_account(account_number)
                        print("--------------------------")
                    else:
                        print("Account not found")
                        print("--------------------------")
                elif (choice==3):
                        banking_system.print_all_users()
                elif (choice==4):
                        print(f"Total Balance: ${banking_system.total_balance()}")
                        print("--------------------------")
                elif (choice==5):
                        print(f"Total Loan: ${banking_system.total_loan_amount()}")
                        print("--------------------------")
                elif (choice==6):
                    print(f"Loan Feature Active: {'Yes' if banking_system.allow_loans else 'No'}")
                    user_input=input("If you want to change Loan feature press Y else type N:")
                    if(user_input=="Y"):
                        banking_system.is_loan_available()
                
                print("1.CREATE AN ACCOUNT")
                print("2.DELETE AN ACCOUNT")
                print("3.ACCOUNTS LIST")
                print("4.CHECK TOTAL BALANCE OF THE BANK")
                print("5.CHECK TOTAL LOAN AMOUNT")
                print("6.LOAN FEATURE OF THE BANK")
                print("0.EXIT")
                print("--------------------------")
                choice = int(input("Enter your choice:"))
                
    print("1.CREATE AN ACCOUNT")
    print("2.DEPOSIT")
    print("3.WITHDRAW")
    print("4.CHECK BALANCE")
    print("5.TRANSACTION HISTORY")
    print("6.APPLY FOR LOAN")
    print("7.BALANCE TRANSFER")
    print("8.Admin")
    print("9.Exit")
    print("--------------------------")

    choice = int(input("Enter your choice:"))
