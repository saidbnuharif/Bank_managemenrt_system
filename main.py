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
        self.balance -= amount

    def add_history(self, message):
        self.history.append(message)

    def remove_message(self):
        return f"{self.name} account removed"


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


current_date = datetime.now().strftime("%d-%m-%Y")
current_time = datetime.now().strftime("%I:%M:%S %p")


while True:

    print("""
    1.Create Account
    2.Deposit
    3.Show Balance
    4.Withdraw
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
        name = input("Enter account name: ").lower()
        for account in data:
            if account["name"] == name:
                bank = Bank(account["name"], account["balance"])
                bank.show_balance()
                break

    elif choice == "4":
        name = input("Enter account holder name: ")
        for account in data:
            if account["name"] == name:
                try:
                    withdrawal_amount = int(input("Enter the amount to withdraw: "))
                except:
                    print("Amount must be numbers only")
                    continue
                Available_balance = account["balance"]
                if Available_balance >= withdrawal_amount:
                    bank = Bank(account["name"], account["balance"])
                    bank.withdraw(withdrawal_amount)
                    account["balance"] = bank.balance
                    account["history"].append(f"Withdrawal ₹{withdrawal_amount}")
                    save_data()
                    print("Money withdrawed successfully")

                elif Available_balance < withdrawal_amount:
                    print("Low balance")

    elif choice == "5":
        for account in data:
            if not data:
                print("List is empty")
            print(f"Name: {account["name"]} | Balance: {account["balance"]}")
        print("Accounts fetched")

    elif choice == "6":
        name = input("Enter account name: ").lower()
        for account in data:
            if account["name"] == name:
                bank = Bank(account["name"], account["balance"], account["history"])
                data.remove(account)
                save_data()
                print(bank.remove_message())
                break
        else:
            print("No account found")

    elif choice == "7":
        name = input("Enter account name: ")
        for account in data:
            if account["name"] == name:
                balance = account["balance"]
                receiver_name = input("Enter receiver account name: ")

                for item in data:
                    if item["name"] == receiver_name:
                        receiver_balance = item["balance"]
                        try:
                            transferring_amount = int(
                                input("Enter money to transfer: ")
                            )
                        except:
                            print("Amount must be numbers only")
                            continue
                        if balance >= transferring_amount:
                            item["balance"] = receiver_balance + transferring_amount
                            account["balance"] = balance - transferring_amount

                            account["history"].append(
                                f"Sent ₹{transferring_amount} to {receiver_name}"
                            )
                            item["history"].append(
                                f"Received ₹{transferring_amount} from {name}"
                            )

                            save_data()
                            print("Amount transferred successfully")

                        else:
                            print("Low balance")
                        break

                else:
                    print("reciver  not found")
                break

        else:
            print("Sender not found")

    elif choice == "8":
        name = input("Enter account name: ")
        for accounts in data:
            if accounts["name"] == name:
                print(f"Transactions: {accounts['history']}")
                break
        else:
            print("No account found")

    elif choice == "9":
        name = input("Enter account name: ").lower()

        for account in data:
            if account["name"] == name:
                for transaction in account["history"]:
                    if "Sent" in transaction:
                        print(transaction)
                break
        else:
            print("Account not found")

    elif choice == "10":
        name = input("Enter account name: ")
        for account in data:
            if account["name"] == name:
                for transaction in account["history"]:
                    if "Received" in transaction:
                        print(transaction)
                    else:
                        print("No money recieved")
            break
        else:
            print("No user found")

    elif choice == "11":
        name = input("Enter account holder name: ")
        for account in data:
            if account["name"] == name:
                for details in account["history"]:
                    if "Deposit" in details:
                        print(details)

                    else:
                        print("No history found")
                    break
            break
        else:
            print("No user found")

    elif choice == "12":
        if not data:
            print("No accounts found")
        else:
            richest_account = data[0]
            for account in data:
                if account["balance"] > richest_account["balance"]:
                    richest_account = account
        print(f"Richest Account: {richest_account}")

    elif choice == "13":
        break

    else:
        print("Invalid input")
        continue
