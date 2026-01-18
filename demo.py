class Employee:
    def __init__(self, name):
        self.name = name
        print("Object Constructed")
    
    def __del__(self):
        print("Object Destroyed")

e1 = Employee("Enrico")
del e1

class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = int(num1)
        self.num2 = int(num2)
        self.num3 = int(num3)
    
    def addition(self):
        print(f"The addition of {self.num1}, {self.num2}, and {self.num3} is equal to", self.num1+self.num2+self.num3)

n1 = Expression("7", "12", "23")
n1.addition()

class Library:
    def __init__(self):
        self.books = ["Python", "Javascript", "C++", "HTML", "Bootstrap", "CSS"]
    
    def display(self):
        if self.books:
            print("\n -- Available books in the database: ")
            for book in self.books:
                print("-", book)
        else:
            print("\n [-- No books are currently available in the database. --]")
    
    def lend(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            
    def returns(self, book_name):
        self.books.append(book_name)
        print(f"\n[-- '{book_name}' has been returned into the database. --]")
    
    def add(self, book_name):
        self.books.append(book_name)
        print(f"\n[-- '{book_name}' has been added into the database. --]")

library = Library()

while True:
    print("[-- Welcome to the Online Library Management System! --]")
    print("[-- What would you like to do today? --]")
    print("<-- {1} Display Books")
    print("<-- {2} Lend Books")
    print("<-- {3} Return Books")
    print("<-- {4} Add Books")
    print("<-- {5} Exit OLMS")
    print("[--------------------------------------]")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        library.display()
    elif choice == 2:
        book = input("-- Enter book name to lend: ")
        library.lend(book)
    elif choice == 3:
        book = input("-- Enter book name to return: ")
        library.returns(book)
    elif choice == 4:
        book = input("-- Enter book name to add: ")
        library.add(book)
    elif choice == 5:
        print("\n [-- Thank you for visiting the Online Library Management System OLMS! --]")
        break
    else:
        print("\n [!-- Invalid option {}. Please enter an eligable value from 1 - 5 --!]")