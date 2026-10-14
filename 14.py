import pickle
class Book(object):
    def __init__(self):
        self.book_id=""
        self.title=""
        self.author_id=""
        self.publisher=""
        self.year_of_publication=""
    def add_book(self):
        self.book_id=input("Enter book id (4 digits): ")
        self.title=input("Enter book title: ")
        self.author_id=input("Enter author id (5 digits): ")
        self.publisher=input("Enter publisher: ")
        self.year_of_publication=input("Enter year of publication: ")
    def display_book(self):
        print("book id: "+self.book_id)
        print("title: "+self.title)
        print("author id: "+self.author_id)
        print("publisher: "+self.publisher)
        print("year of publication: "+self.year_of_publication)

myBook=[]
book=Book()

class Author(object):
    def __init__(self):
        self.author_id=""
        self.author_name=""
        self.affiliation=""
        self.country=""
        self.phone=""
        self.email=""
    def add_author(self):
        self.author_id=input("Enter author id (5 digits: ")
        self.author_name=input("Enter author name: ")
        self.affiliation=input("Enter affiliation: ")
        self.country=input("Enter country: ")
        self.phone=input("Enter phone number: ")
        self.email=input("Enter email: ")
    def display_author(self):
        print("id: "+self.author_id)
        print("name: "+self.author_name)
        print("affiliation: "+self.affiliation)
        print("country: "+self.country)
        print("phone: "+self.phone)
        print("email: "+self.email)

myAuthor=[]
author=Author()

class User(object):
    def __init__(self):
        self.user_id=""
        self.user_name=""
        self.password=""
        self.email=""
        self.address=""
        self.phone=""
        self.email=""
    def add_user(self):
        self.user_id=input("Enter user id: ")
        self.user_name=input("Enter user name: ")
        self.password=input("Enter password: ")
        self.email=input("Enter email: ")
        self.address=input("Enter address: ")
        self.phone=input("Enter phone: ")
    def display_user(self):
        print("id:"+self.user_id)
        print("name: "+self.user_name)
        print("password: "+self.password)
        print("email: "+self.email)
        print("address: "+self.address)
        print("phone: "+self.phone)
        print("email: "+self.email)

myUser=[]
user=User()

#main code
while True:
    print("1.Add Book")
    print("2.Add Author")
    print("3.Add User")
    print("4.Display Books")
    print("5.Display Authors")
    print("6.Display Users")
    print("7.Exit")
    choice=input("Enter choice: ")
    if choice=="1":
        book.add_book()
        file1 = open("mybooks.dat", "ab")
        pickle.dump(book, file1)
        file1.close()
    elif choice=="2":
        author.add_author()
        file1 = open("myauthors.dat", "ab")
        pickle.dump(Author(), file1)
        file1.close()
    elif choice=="3":
        user.add_user()
        file1 = open("myusers.dat", "ab")
        pickle.dump(User(), file1)
        file1.close()
    elif choice=="4":
        book.display_book()
        file2 = open("mybooks.dat", "rb")
        while True:
            try:
                data = pickle.load(file2)
                print(data.book_id)
                print(data.title)
                print(data.author_id)
                print(data.publisher)
                print(data.year_of_publication)
            except(EOFError):
                break
        file2.close()
    elif choice=="5":
        author.display_author()
        file2 = open("myauthors.dat", "rb")
        while True:
            try:
                data = pickle.load(file2)
                print(data.author_id)
                print(data.author_name)
                print(data.affiliation)
                print(data.country)
                print(data.phone)
                print(data.email)
            except(EOFError):
                break
        file2.close()
    elif choice=="6":
        user.display_user()
        file2 = open("myusers.dat", "rb")
        while True:
            try:
                data = pickle.load(file2)
                print(data.user_id)
                print(data.user_name)
                print(data.password)
                print(data.email)
                print(data.address)
                print(data.phone)
                print(data.email)
            except(EOFError):
                break
        file2.close()
    elif choice=="7":
        break
    else:
        print("Invalid choice")