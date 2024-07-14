class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" *"+book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued{bookName}.!!!")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is already booked")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book")

class Student:
    def requestBook(self):
        self.book = input("Enter the boook name you want to burrow: ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the boook name you want to return: ")
        return self.book

if __name__ == "__main__":
    centraLibrary = Library(["Algorithms","data structure and Algorithms","Algorithms1","Algorithms2","Algorithms3","Algorithms4","Django"])
    # centraLibrary.displayAvailableBooks()
    while(True):
        wlcMsg = '''***Welcome to Central Library***
        Please choose an Option:
        1. Listing all the books
        2. Request a book
        3. Return a book
        4. Exit the Library
        '''
        print(wlcMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook()
        elif a == 3:
            centraLibrary.returnBook()
        elif a == 4:
            print("Thanks for choosing Central Library. Stay Liberated!")
            exit()
        else:
            print("Invalid Choice")

        