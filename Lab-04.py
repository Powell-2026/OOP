import pickle
class Customer(object):
    def __init__(self):
        self.cid=""
        self.cname=""
        self.acc_no=""
        self.balance=""
        self.credit_card=[]
    def create_account(self):
        self.cid=input("Enter Customer ID: ")
        self.cname=input("Enter Customer Name: ")
        self.acc_no=input("Enter Customer Account Number: ")
        self.balance=input("Enter Customer Balance: ")
    def transfer_funds(self,bene_cust_obj,amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount >self.balance:
            print("Insufficient funds.")
        else:
            self.balance-=amount
            bene_cust_obj.balance+=amount
            print("Transfer Successful.")
    def assign_card(self,card_obj):
        self.credit_card.append(card_obj)
    def display_customers(self):
        print("Customer ID:",self.cid)
        print("Customer Name:",self.cname)
        print("Customer Account Number:",self.acc_no)
        print("Balance:",self.balance)
        print("Credit Card:",self.credit_card)

class Card(object):
    def __init__(self):
        self.card_no=""
        self.ccv=""
        self.expiration_date=""
        self.balance=""
    def create_card(self):
        self.card_no=input("Enter Card Number: ")
        self.ccv=input("Enter CCV: ")
        self.expiration_date=input("Enter Expiration Date: ")
        self.balance=input("Enter Balance: ")
    def display_card(self):
        print("Card Number:",self.card_no)
        print("CCV:",self.ccv)
        print("Expiration Date:",self.expiration_date)
        print("Balance:",self.balance)
customer = Customer()
card = Card()
#
while True:
    print("1. Create Customer")
    print("2. Create Card")
    print("3. Transfer funds")
    print("4. Assign Card")
    print("5. Display Customers")
    print("6. Display Cards")
    print("7. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        customer.create_account()
        f1=open("customer.dat","ab")
        pickle.dump(customer,f1)
        f1.close()

    elif choice=="2":
        card.create_card()
        f1=open("card.dat","ab")
        pickle.dump(card,f1)
        f1.close()

    elif choice == "3":
        sender_id = input("Enter Sender Customer ID: ")
        receiver_id = input("Enter Recipient Customer ID: ")
        customers = []
        try:
            with open("customer.dat", "rb") as f2:
                while True:
                    try:
                        data = pickle.load(f2)
                        data.balance = float(data.balance)
                        customers.append(data)
                    except EOFError:
                        break
        except FileNotFoundError:
            print("No customer file found.")
            continue
        sender = None
        recipient = None
        for cust in customers:
            if cust.cid == sender_id:
                sender = cust
            if cust.cid == receiver_id:
                recipient = cust
        if sender is None:
            print("Sender Customer ID not found.")
        elif recipient is None:
            print("Recipient Customer ID not found.")
        elif sender is recipient:
            print("Cannot transfer money to the same account.")
        else:
            amount = float(input("Enter amount to transfer: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
            elif amount > sender.balance:
                print("Insufficient funds.")
            else:
                sender.transfer_funds(recipient, amount)
                with open("customer.dat", "wb") as f2:
                    for cust in customers:
                        pickle.dump(cust, f2)
                print("Updated balances:")
                print(sender.cname, sender.balance)
                print(recipient.cname, recipient.balance)

    elif choice == "4":
        customer_id = input("Enter Customer ID: ")
        card_number = input("Enter Card Number to Assign: ")
        customers = []
        cards = []
        try:
            with open("customer.dat", "rb") as f:
                while True:
                    try:
                        customers.append(pickle.load(f))
                    except EOFError:
                        break
        except FileNotFoundError:
            print("No customer file found.")
            continue
        try:
            with open("card.dat", "rb") as f:
                while True:
                    try:
                        cards.append(pickle.load(f))
                    except EOFError:
                        break
        except FileNotFoundError:
            print("No card file found.")
            continue
        selected_customer = None
        for cust in customers:
            if cust.cid == customer_id:
                selected_customer = cust
                break
        selected_card = None
        for c in cards:
            if c.card_no == card_number:
                selected_card = c
                break
        if selected_customer is None:
            print("Customer ID not found.")
        elif selected_card is None:
            print("Card number not found.")
        elif any(c.card_no == selected_card.card_no
                 for c in selected_customer.credit_card):
            print("This card is already assigned to this customer.")
        else:
            selected_customer.assign_card(selected_card)
            with open("customer.dat", "wb") as f:
                for cust in customers:
                    pickle.dump(cust, f)
            print("Card assigned successfully!")

    elif choice=="5":
        customer.display_customers()
        f2=open("customer.dat","rb")
        while True:
            try:
                data=pickle.load(f2)
                print(data.cid)
                print(data.cname)
                print(data.acc_no)
                print(data.balance)
                print(data.credit_card)
            except(EOFError):
                break
        f2.close()

    elif choice=="6":
        card.display_card()
        f2=open("card.dat","rb")
        while True:
            try:
                data=pickle.load(f2)
                print(data.card_no)
                print(data.ccv)
                print(data.expiration_date)
                print(data.balance)
            except(EOFError):
                break
        f2.close()

    elif choice=="7":
        break

    else:
        print("Invalid choice")


