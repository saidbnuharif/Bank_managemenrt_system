import json

with open("Bank_app.json", "r", encoding="utf-8") as file:
    data = json.load(file)


class Bank:

    def __init__(self, name, balance, history):

        self.name = name
        self.balance = balance
        self.history = history

    def show_balance(self):

        print(f"Name: {self.name}")
        print(f"Balance: ₹{self.balance}")

    def deposit(self, amount):
        self.balance += amount

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
    12.Riches account     
    13.Exit                                        
    """)

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter account holder name: ").lower()
        for account in data:
            if account["name"] == name:
                print("Account already exists")
                break
        else:
            try:
                balance = int(input("Enter money to deposit: "))
            except:
                print("Balance must be numbers only")
                continue

            bank = Bank(name, balance)
            data.append({"name": bank.name, "balance": bank.balance, "history": []})
            save_data()
            print("Account created")

    elif choice == "2":
        name = input("Enter account name: ")
        for account in data:
            if account["name"] == name:
                try:
                    amount = int(input("Enter amount to deposit: "))
                except:
                    print("Amount must be numbers only")
                    continue
                bank = Bank(account["name"], account["balance"], account["history"])
                bank.deposit(amount)
                account["balance"] = bank.balance
                bank.add_history(f"Deposit ₹{amount}")
                account["balance"] = bank.balance
                account["history"] = bank.history
                save_data()
                print("Amount deposit success")
                break

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
