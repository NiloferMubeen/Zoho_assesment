

class Library:
    
            def __init__(self,books):
                self.books = books
                    
            def display(self):
                print()
                print('-----------------')
                print('Available Books:')
                print('-----------------')
                for book in self.books:
                    print(book)
                    
            def lend_book(self,requestedBook):
                count = 0
                for book in requestedBook:
                    if book in self.books:
                        count += 1
                        print(f'{book}: Available')
                        self.books.remove(book)
                    else:
                        print()
                        print()
                        print(f'Sorry , the {book} is/are not available now')
                print(f'You have now borrowed {count} books')   
                
                 
            def update_book(self,returnedBook):
                for book in returnedBook:
                    self.books.append(book)
                print()
                print('Thank you for returning')
                
                
        
class Customer:
    
    def __init__(self):
        self.borrow_history = {}
    
    def user_registration(self,name):
            if name not in self.borrow_history.keys():
                self.name = name
                self.borrow_history[self.name] = []
                
                print('REGISTRATION SUCCESSFUL !!')
                
            else:
                print()
                print('Username already exists')
           
    def user_login(self,name):
        if name in self.borrow_history.keys():
            print('--------------------------')
            print('Authentication Successful!')
            print('--------------------------')
            return True
        else:
            print()
            print('Authentication FAILED . Kindly Register to Borrow Books')
            print()
            option = input('Would you like to register? : (Y/N) : ')
            if option == 'Y':
                self.user_registration(name)
            else:
                return False
                
    def display_history(self,name):
        if name in self.borrow_history.keys():
            if len(self.borrow_history[name]) != 0 :
                for i in self.borrow_history[name]:
                        print(i)
            else:
                print()
                print('No previous History')
        
    def requestBook(self):
        print()
        print('Enter the name of the books you need')
        self.book = list(input().split(','))
        
        if len(self.book) > 5:
            print("Sorry you are allowed to borrow upto 5 Books")
        else:
            self.borrow_history[self.name].append(self.book)
        return self.book    
    
        
    def returnBook(self):
        print()
        print('Enter the name of the books you need to return')
        self.returned = list(input().split(','))
        return self.returned
    
books = ['Blood Line','Davinci Code','Angels and Demons','Five point someone','The Alchemist','Harry Potter','The Chronicles of Narnia']   

lib = Library(books)

cust = Customer()


while True:
    print('\t\t-----------------------------')
    print('\t\t Library Management System')
    print('\t\t-----------------------------')
    
    print('\n\n')
    
    print('Enter 1 Register')
    print()
    print('Enter 2 to Login')
    print()
    option = int(input('Enter an option:'))
    
    if option == 1:
        print()
        name = input('Enter your Name:')
        cust.user_registration(name)
    if option == 2:
        print()
        name = input('Enter your name:')
        authentication_status = cust.user_login(name)
        
        if authentication_status:
    
            while True:
                print('------------------------------------------')
                print('WELCOME USER. Now you can pick one option')
                print('------------------------------------------')
            
                print('Enter 1 to display the books')
                print('Enter 2 to Borrow a book')
                print('Enter 3 to return a book')
                print('Enter 4 to display Borrow history')
                print('Enter 5 to exit')
                print('\n\n')
                print('---------------------------------')
                
                choice = int(input('Enter your Option:'))

                if choice == 1:
                    print('You may borrow upto 5 books')
                    lib.display()
                if choice == 2:
                    requestedBook = cust.requestBook()
                    lib.lend_book(requestedBook)
                if choice == 3:
                    returnedBook = cust.returnBook()
                    lib.update_book(returnedBook)
                if choice == 4:
                    cust.display_history(name)
                if choice == 5:
                    print('Thank you! Bye!')
                    quit()
