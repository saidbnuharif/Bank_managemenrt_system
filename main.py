import json
from datetime import datetime


def load_data():
    try:
        with open("Bank_app.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except ValueError:
        return []


data = load_data()


class Bank:

    def __init__(self, account_no, name, balance, history):

        self.Account_number = account_no
        self.name = name
        self.balance = balance
        self.history = history

    def show_balance(self):

        print(f"Name: {self.name}")
        print(f"Balance: ₹{self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Please enter amount grater that zero")
            return
        self.balance += amount
        current_time = datetime.now().strftime("%I:%M:%S %p")
        current_date = datetime.now().strftime("%d-%m-%Y")
        self.history.append(f"₹{amount} deposited at {current_time} on {current_date}")
        print("Amount deposited successfully")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero")
            return
        if self.balance < amount:
            print("Insufficient balance")
            return
        self.balance -= amount
        current_time = datetime.now().strftime("%I:%M:%S %p")
        current_date = datetime.now().strftime("%d-%m-%Y")
        self.history.append(f"₹{amount} withdrawn at {current_time} on {current_date}")
        print("Amount withdrawn successfully")

    from datetime import datetime

    def sendMoney(self, receiver, amount):

        if amount <= 0:
            print("Amount must be greater than zero")
            return
        if self.balance < amount:
            print("Insufficient balance")
            return
        self.balance -= amount
        receiver.balance += amount
        current_time = datetime.now().strftime("%I:%M:%S %p")
        current_date = datetime.now().strftime("%d-%m-%Y")
        self.history.append(
            f"₹{amount} sent to {receiver.name} ({receiver.Account_number}) at {current_time} on {current_date}"
        )
        receiver.history.append(
            f"₹{amount} received from {self.name} ({self.Account_number}) at {current_time} on {current_date}"
        )
        print("Money transferred successfully")

    def add_history(self, message):
        self.history.append(message)

    def remove_message(self):
        return f"{self.Account_number} account removed"


def save_data():

    with open("Bank_app.json", "w", encoding="utf-8") as file:

        json.dump(data, file, indent=4, ensure_ascii=False)

        print("data saved")


# def find_account():
#     try:
#         account_number = int(input("Enter account number"))
#     except ValueError:
#         print("Account number must be numbers only")
#         return
#     for accounts in data:
#         if accounts["Account_number"] == account_number:
#             return accounts
#     else:
#         return "No account found"


while True:

    print("""
    1.Create Account
    2.Deposit     
    3.Withdraw
    4.Show Balance
    5.Show all account
    6.Remove
    7.Transfer money
    8.Transaction            
    9.Sended
    10.Recieved
    11.Deposits
    12.Richest account     
    13.Exit                                        
    """)

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter accound holder name: ")
        try:
            balance = int(input("Enter the balance: "))
        except:
            print("Balance must be number only: ")
            continue
        if not data:
            account_no = 111110
        else:
            account_no = data[-1]["Account_number"] + 1
        bank = Bank(account_no, name, balance, [])
        data.append(
            {
                "Account_number": bank.Account_number,
                "name": bank.name,
                "balance": bank.balance,
                "history": bank.history,
            }
        )
        save_data()
        print("Account created successfully")

    elif choice == "2":
        try:
            account_no = int(input("Enter account number: "))
        except ValueError:
            print("Account number must be numbers only")
            continue
        for accounts in data:
            if accounts["Account_number"] == account_no:
                try:
                    amount = float(input("Enter the amount to deposit: "))
                except:
                    print("Amount must be numbers only")
                    continue
                account = Bank(
                    accounts["Account_number"],
                    accounts["name"],
                    accounts["balance"],
                    accounts["history"],
                )
                account.deposit(amount)
                accounts["balance"] = account.balance
                accounts["history"] = account.history
                save_data()
                break
        else:
            print("No account found")

    elif choice == "3":
        try:
            account_no = int(input("Enter account number: "))
        except ValueError:
            print("Account number must be numbers only")
            continue
        for accounts in data:
            if accounts["Account_number"] == account_no:
                try:
                    amount = float(input("Enter amount to transfer: "))
                except ValueError:
                    print("Amount must be numbers only")
                    break
                account = Bank(
                    accounts["Account_number"],
                    accounts["name"],
                    accounts["balance"],
                    accounts["history"],
                )
                account.withdraw(amount)
                accounts["balance"] = account.balance
                accounts["history"] = account.history
                save_data()
                break
        else:
            print("No account found")

    elif choice == "4":
        try:
            account_no = int(input("Enter account number: "))
        except ValueError:
            print("Account number must be numbers only")
            continue
        for accounts in data:
            if accounts["Account_number"] == account_no:
                account = Bank(
                    accounts["Account_number"],
                    accounts["name"],
                    accounts["balance"],
                    accounts["history"],
                )
                account.show_balance()
                break
        else:
            print("No account found")

    elif choice == "5":
        if not data:
            print("No data found")
            continue
        else:
            for accounts in data:
                print(f"Account number: {accounts['Account_number']}")
                print(f"Account name: {accounts['name']}")
                print(f"Account balance: {accounts['balance']:,}")
                print(f"Account history: {accounts['history']}")
                print("-----------------------------------------")

    elif choice == "6":
        try:
            account_no = int(input("Enter account number: "))
        except ValueError:
            print("Account number must be numbers only")
            continue
        for accounts in data:
            if accounts["Account_number"] == account_no:
                account = Bank(
                    accounts["Account_number"],
                    accounts["name"],
                    accounts["balance"],
                    accounts["history"],
                )
                data.remove(accounts)
                print(f"{account_no} removed from database")
                save_data()
                break
        else:
            print("No account found")

    elif choice == "7":
        try:
            sender_account_no = int(input("Enter sender account number: "))
        except ValueError:
            print("Account number must be numbers only")
            continue
        try:
            receiver_account_no = int(input("Enter receiver account number: "))
        except ValueError:
            print("Account number must be numbers only")
            continue
        if sender_account_no == receiver_account_no:
            print("Sender and receiver cannot be the same")
            continue
        sender_account = None
        receiver_account = None
        for account in data:
            if account["Account_number"] == sender_account_no:
                sender_account = account
            if account["Account_number"] == receiver_account_no:
                receiver_account = account
        if sender_account is None:
            print("Sender account not found")
            continue
        if receiver_account is None:
            print("Receiver account not found")
            continue
        try:
            amount = float(input("Enter amount to send: "))
        except ValueError:
            print("Amount must be numbers only")
            continue
        sender = Bank(
            sender_account["Account_number"],
            sender_account["name"],
            sender_account["balance"],
            sender_account["history"],
        )
        receiver = Bank(
            receiver_account["Account_number"],
            receiver_account["name"],
            receiver_account["balance"],
            receiver_account["history"],
        )
        sender.sendMoney(receiver, amount)
        sender_account["balance"] = sender.balance
        sender_account["history"] = sender.history

        receiver_account["balance"] = receiver.balance
        receiver_account["history"] = receiver.history

        save_data()

        print("Transfer completed")

    elif choice == "13":
        break

    else:
        print("Invalid input")
        continue
