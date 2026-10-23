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
        self.balance-=amount
        bene_cust_obj.balace+=amount
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
    elif choice=="3":
        id = input("Enter Customer ID: ")
        f2=open("customer.dat","rb")
        data=pickle.load(f2)
        for i in f2:
            if id == i.data.cid:
                bene_cust_obj=i
            else:
                print("Invalid Customer ID")
        customer.transfer_funds(bene_cust_obj,amount=int(input("Enter amount to transfer: ")))
        f2.close()
    elif choice=="4":
        customer.assign_card(customer.cid)
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


