
class User:
    def __init__(self,name , email, address, account_type, bank) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.account_no=len(bank.users)+ 1
        self.balance=0
        self.bank=bank
        self.statement=[]

    def deposit(self,amount):
        if amount > 0:import random
class User:
    def __init__(self,name , email, address, account_type, bank) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.account_no=self.generate_account_number()
        self.balance=0
        self.bank=bank
        self.statement=[]

    def generate_account_number(self):
        return str(random.randint(10**10, 10**11 - 1))

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print("-------Deposit Done------")
            self.statement.append(f"Deposit: ${amount}")
        else:
            print("Negative amount not accepted")

    def withdraw(self,amount):
        if amount > 0:
            if (amount > self.balance):
                print("Withdraw amount exceeded")
            else:
                self.balance-=amount
                print("------Withdraw successful------")
                self.statement.append(f"Withdraw: ${amount}")
        else:
            print("Negative amount not accepted")

    def available_balance(self):
        print(f"{self.name} Available Balance: {self.balance}")

    def transfer(self,user,amount):
        if amount> 0:
            if (amount <= self.balance):
                if user in self.bank.users:
                    self.balance -= amount
                    user.balance += amount
                    self.statement.append(f"Transfer ${amount} to a/c no:{user.account_no}")
                else:
                    print("Account does not exist")
            else:
                print("Withdraw amount exceeded")
        else:
            print("Negative amount not accepted")
    
    def loan_request(self,amount):
        if self.bank.is_loan_enabled:
            if amount > 0 and len(self.bank.loans)<2:
                self.bank.loans[self]=amount
                self.balance+=amount
                print("Loan request accepted")
                self.statement.append(f"Received a loan of ${amount}")
            elif len(self.bank.loans)>=2:
                print("You already cross the limit of maximum number of loans")
            else:
                print("Loan request not accepted")

    def view_statement(self):
        for stat in self.statement:
            print(stat)
class Bank:
    def __init__(self) -> None:
        self.users=[]
        self.loans={}
        self.is_bankrupt=False
        self.is_loan_enabled=True

    def create_user(self,name,email,address,acount_type):
        user=User(name,email,address,acount_type,self)
        self.users.append(user)
        print("user created: ",user)
        return user

    def delete_user(self,user):
        if user in self.users:
            self.users.remove(user)
            print("User deleted successfully")
        else:
            print("User not found")

    def total_balance(self):
        balance=sum(user.balance for user in self.users)
        print(balance)

    def total_loan(self):
        loan=sum(self.loans.values())
        print(loan)

    def print_users(self):
        for user in self.users:
            print(f"{user.name} {user.email} {user.address} {user.account_type}" )
    
# user=User()
admin = Bank()
user1 = admin.create_user("Tamim", "tamim122@example.com", "Address 1", "Savings")
user2 = admin.create_user("Alen", "alen2@example.com", "Address 2", "Current")
admin.print_users()

user1.deposit(1000)
user1.withdraw(100)
user1.transfer(user2,500)

user1.available_balance()
user2.available_balance()

user1.view_statement()
user2.loan_request(200)
    
            self.balance += amount
            self.statement.append(f"Deposit ${amount}")
        else:
            print("Negative amount not accepted")

    def withdraw(self,amount):
        if amount > 0:
            if (amount > self.balance):
                print("Withdraw amount exceeded")
            else:
                self.balance-=amount
                self.statement.append(f"Withdraw: ${amount}")
        else:
            print("Negative amount not accepted")

    def available_balance(self):
        print(self.balance)

    def transfer(self,user,amount):
        if amount> 0:
            if (amount <= self.balance):
                if user in self.bank.users:
                    self.balance -= amount
                    user.balance += amount
                    self.statement.append(f"Transfer ${amount} to {user.account_no}")
                else:
                    print("Account does not exist")
            else:
                print("Withdraw amount exceeded")
        else:
            print("Negative amount not accepted")
    
    def loan_request(self,amount):
        if self.bank.is_loan_enabled:
            if amount > 0 and len(self.bank.loans)<2:
                self.bank.loans[self]=amount
                self.balance+=amount
                self.statement.append(f"Received a loan of ${amount}")
            elif len(self.bank.loans)>=2:
                print("You already cross the limit of maximum number of loans")
            else:
                print("Loan request not accepted")

    
class Bank:
    def __init__(self) -> None:
        self.users=[]
        self.loans={}
        self.is_bankrupt=False
        self.is_loan_enabled=True

    def create_user(self,name,email,address,acount_type):
        user=User(name,email,address,acount_type,self)
        self.users.append(user)
        print("user created: ",user)
        return user

    def delete_user(self,user):
        if user in self.users:
            self.users.remove(user)
            print("User deleted successfully")
        else:
            print("User not found")

    def total_balance(self):
        balance=sum(user.balance for user in self.users)
        print(balance)

    def total_loan(self):
        loan=sum(self.loans.values())
        print(loan)

    def print_users(self):
        for user in self.users:
            print(f"{user.name} {user.email} {user.address} {user.account_type}" )
    
admin = Bank()
user1 = admin.create_user("Tamim", "user1@example.com", "Address 1", "Savings")
user2 = admin.create_user("Alen", "user2@example.com", "Address 2", "Current")
admin.print_users()

user1.deposit(1000)
user1.transfer(user2,500)

user1.available_balance()
user2.available_balance()
    
