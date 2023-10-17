import random
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
            self.bank.bank_total_balance += amount
            print("---------------")
            print("Deposit Done")
            print("---------------")
            self.statement.append(f"Deposit: ${amount}")
        else:
            print("Negative amount not accepted")

    def withdraw(self,amount):
        if amount > 0:
            if (amount > self.balance):
                print("Withdraw amount exceeded")
            else:
                self.balance-=amount
                self.bank.bank_total_balance -= amount
                print("---------------")
                print("Withdraw successful")
                print("---------------")
                self.statement.append(f"Withdraw: ${amount}")
        else:
            print("Negative amount not accepted")

    def available_balance(self):
        print("---------------")
        print(f"{self.name} Available Balance: {self.balance}")
        print("---------------")

    def transfer(self,user_email,amount):
        if amount> 0:
            if (amount <= self.balance):
                for user in self.bank.users:
                    if user.email==user_email:
                        self.balance -= amount
                        user.balance += amount
                        self.statement.append(f"Transfer ${amount} to a/c no:{user.account_no} successful :) ")
                else:
                    print("Account does not exist")
            else:
                print("Your balance is too low to transfer")
        else:
            print("Negative amount not accepted")
    
    def loan_request(self,amount):
            if amount > 0 and len(self.bank.loans)<2:
                self.bank.loans[self]=amount
                self.balance += amount
                self.bank.total_loan_amount += amount
                print("---------------")
                print("Loan request accepted")
                print("---------------")
                self.statement.append(f"---Received a loan of ${amount}---")
            elif len(self.bank.loans)>=2:
                print("-------You already cross the limit of maximum number of loans------")
            else:
                # print("--------Loan request not accepted--------")
                print("---------------")
                print("Loan request not accepted ,Sorry !!!")
                print("---------------")
    def view_statement(self):
        for stat in self.statement:
            print(stat)

class Bank:
    def __init__(self):
        self.users=[]
        self.loans={}
        self.is_bankrupt=False
        self.is_loan_enabled=True
        self.bank_total_balance=0
        self.total_loan_amount=0

    def create_user(self,name,email,address,acount_type):
        user=User(name,email,address,acount_type,self)
        self.users.append(user)
        print("user created successfully: ",user.name)
        print("-----------------------------")
        return user

    def delete_user(self,user_email):
        for user in self.users:
            if user.email==user_email:
                self.users.remove(user)
                print("---------------")
                print("User deleted successfully")
                print("---------------")
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
            print(f"{user.name} {user.email} {user.address} {user.account_type} {user.account_no}" )
            print("-----------------------------")
    
    def toggle_loan(self,enable):
        self.is_loan_enabled=enable

admin = Bank()

# user1.transfer(user2,500)


print("1.CREATE AN ACCOUNT")
print("2.DEPOSIT")
print("3.WITHDRAW")
print("4.CHECK BALANCE")
print("5.TRANSACTION HISTORY")
print("6.APPLY FOR LOAN")
print("7.BALANCE TRANSFER")
print("8.ADMIN PANEL")
print("9.Exit")

choice=int(input("Enter your choice:"))
print("-----------------------------")
while(choice!=9):

    if(choice==1):
        name=input("Enter name:")
        email=input('Enter your email:')
        address=input("Enter your address:")
        account_type=input("Account type:")
        user = admin.create_user(name,email,address,account_type)
    elif(choice==2):
        deposit_amount=int(input('Enter amount to deposit:'))
        user.deposit(deposit_amount)
    elif(choice==3):
        withdraw_amount=int(input('Enter withdraw amount:'))
        user.withdraw(withdraw_amount)
    elif(choice==4):
        user.available_balance()
    elif(choice==5):
        user.view_statement()
    elif(choice==6):
        if(user.bank.is_loan_enabled):
            loan_amount=int(input('Enter loan amount:'))
            user.loan_request(loan_amount)
        else:
            print("Currently loan system OFF :( ")
            print("-----------------------------")
    elif(choice==7):
        transfer_amount=int(input('Enter amount to transfer:'))
        transfer_email=input("Enter email you want to transfer this amount:")
        user.transfer(transfer_email,transfer_amount)
    elif(choice==8): #admin panel
        print("------Admin Panel-------")
        print("1.CREATE AN ACCOUNT")
        print("2.DELETE AN ACCOUNT")
        print("3.SEE ACCOUNT LIST")
        print("4.BANK AVAILABLE BALANCE")
        print("5.TOTAL LOAN AMOUNT")
        print("6.LOAN ON OFF")
        print("7.Exit")
        
        choice=int(input("Enter your choice:"))
        print("-----------------------------")

        while(choice!=7):

            if(choice==1):
                name=input("Enter name:")
                email=input('Enter your email:')
                address=input("Enter your address:")
                account_type=input("Account type:")
                user = admin.create_user(name,email,address,account_type)
            elif(choice==2):
                delete_email=input("Enter email to delete your account:")
                admin.delete_user(delete_email)
            elif(choice==3):
                admin.print_users()
            elif(choice==4):
                print("---------------")
                print("Total Balance: ",admin.bank_total_balance)
                print("---------------")
            elif(choice==5):
                print(admin.total_loan_amount)
            elif(choice==6):
                loan_on_off=input('Enter loan On or Off:').lower()
                print("-----------------------------")
                if(loan_on_off=="on"):
                    admin.toggle_loan(True)
                elif(loan_on_off=="off"):
                    admin.toggle_loan(False)

            print("1.CREATE AN ACCOUNT")
            print("2.DELETE AN ACCOUNT")
            print("3.SEE ACCOUNT LIST")
            print("4.BANK AVAILABLE BALANCE")
            print("5.TOTAL LOAN AMOUNT")
            print("6.LOAN ON OFF")
            print("7.LOGOUT FROM ADMIN PANEL")
            
            choice=int(input("Enter your choice:"))
            print("-----------------------------")
            # admin panel end

    print("1.CREATE AN ACCOUNT")
    print("2.DEPOSIT")
    print("3.WITHDRAW")
    print("4.CHECK BALANCE")
    print("5.TRANSACTION HISTORY")
    print("6.APPLY FOR LOAN")
    print("7.BALANCE TRANSFER")
    print("8.ADMIN PANEL")
    print("9.Exit")

    choice=int(input("Enter your choice:"))
    print("-----------------------------")
    
