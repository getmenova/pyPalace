class Library:
    def __init__(self,listOfBooks):
        self.avaliableBooks = listOfBooks

    def display_avaliable_books(self):
        print()
        print("Avaliable Books")
        for book in self.avaliableBooks:
            print (book) 

    def lend_book(self,requestedBook):
        if requestedBook in self.avaliableBooks:
            print("You have now borred the book")
            self.avaliableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not avaliable in our list")
        
    def add_book(self,returnedBook):
        self.avaliableBooks.append(returnedBook)
        print("You have returned the book.Thank you.")

class Customer:
    def request_book(self):
        print("Enter the name of a book you would like to borrow: ")
        self.book = input()
        return self.book

    def return_book(self):
        print('Enter the name of the book which tou are returning')
        self.book = input()
        return self.book


library = Library(['Think and Grow Rich','Who will cry when you die','For One more day'])
customer = Customer()


print("Enter 1 to display the avaliable books")
print("Enter 2 to request for a book")
print("Enter 3 to return a book")
print("Enter 4 to exit")
while True:    
    user_choice = int(input())
    if user_choice is 1:
        library.display_avaliable_books()
    elif user_choice is 2:
        requested_book = customer.request_book()
        library.lend_book(requested_book)
    elif user_choice is 3:
        returnedBook = customer.request_book()
        library.add_book(returnedBook)
    elif user_choice is 4:
        quit()