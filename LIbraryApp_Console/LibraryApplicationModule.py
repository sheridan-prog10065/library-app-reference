"""
Module that defines the LibraryApplication class

Author: Prof. Magdin Stoica
E-Mail: magdin.stoica@sheridancollege.ca
Version 1.0 (Python)
"""
from LibraryModule import Library
from ExceptionsModule import OperationCancel
from BookModule import Book
from LibraryAssetModule import LibraryAsset
from ExceptionsModule import InvalidTransaction

class LibraryApplication:
    """
    The LibraryApplication class represents an application used in a library that allows librarians
    to register, loan and return books for library users. The class displays and performs the the library management 
    functions on a given book: checking status, borrowing and returning a book
    
    Attributes:
        _library : Library  -- the library object that holds the books and all library assets
    
    Author: Magdin Stoica
    Version 1.0 (Python)
    """

    #these are class variables which are not specific to an instance, they are not field variables
    #they are shared by all instances and are accessible using the name of the class with the DOT notation

    #create the MAIN MENU options
    SELECT_BOOK_OPTION = 1
    REGISTER_BOOK_OPTION = 2
    EXIT_APPLICATION_OPTION = 3

    #crate the BOOK MENU option
    CHECK_STATUS_OPTION = 1
    BORROW_OPTION = 2
    RETURN_OPTION = 3
    DISPLAY_BOOK_ASSETS = 4
    EXIT_BOOK_MENU_OPTION = 5
    
    def __init__(self):
        """Initialize the field variables of the library object,"""        
        
        #the library this application allows the user to use and manage
        self._library = None
    

    def run(self):
        """
        The entry point into the application object. Ensures that all other code is protected against
        unhandled exceptions.
        """
        #use exception handling to ensure the application does not crash
        try:
            #create the library object that will be used throughout the application
            #NOTE: Why is it better to create it here rather than in the app constructor?
            self._library = Library()

            #open the library for business
            self.open()

        except Exception as e:
            print('An error occurred with the following message: ', e)
    

    def open(self):
        """
        Starts the library user interaction by displaying the required user options. 
        User navigates the menus managing books and providing library services
        """ 
        #keep displaying the menu until the user chooses to exit the application
        while True:
            #display the main menu and perform the main actions depending on the user's choice
            selectedOption = self.showMainMenu()

            if selectedOption == LibraryApplication.SELECT_BOOK_OPTION:
                book = self.onSelectBook()
                if book != None:
                    self.manageBook(book)
            elif selectedOption == LibraryApplication.REGISTER_BOOK_OPTION:
                self.onRegisterBook()
            elif selectedOption == LibraryApplication.EXIT_APPLICATION_OPTION:
                #the application is shutting down
                return
            else:
                #go again when the user choose 3 instead of 1 or 2
                print('Please enter a valid menu option', "\n")


    def showMainMenu(self):
        """
        Displays the Main Library Menu and ensure the user picks an option. Handles invalid input but doesn't check
        that the menu option is one of the displayed ones which is left for the caller.
        Returns:
            the option selected by the user
        """
        while True:
            try:
                return int(input('\nMain Menu\n\n1: Select Book\n2: Register Book\n3: Exit\n\nEnter a choice: ')) 
            except ValueError:
                #if the user enters "abc" instead of a number
                print("Please enter a valid menu option.", "\n")
        

    def showBookMenu(self):
        """
        Displays the Book Menu that allows the user to perform book operations. Handles invalid input but doesn't check
        that the menu option is one of the displayed ones which is left for the caller
        Returns:
            the option selected by the user
        """
        while True:
            try:
                return int(input('\nBook Menu\n\n1: Check Status\n2: Borrow Book\n3: Return Book\n4: Display Book Assets\n5: Exit\n\nEnter a choice: ')) 
            except ValueError:
                #if the user enters "abc" instead of a number
                print("Please enter a valid menu option.", "\n")
        

    def onRegisterBook(self):
        """Registers a new book into the library. The user is prompted for all book information including the type of book to register.
        The method obtains all neccessary information and requries the library to register a book given the 
        information provided by the user. The method is therefore responsible for the user interaction but not
        the business logic
        """
        print("Exercise: implement the intractivity and business logic necessary for adding a new book")

    def onSelectBook(self):
        """Select a book by prompting the user for the book information and remembering which book was selected.
        Prompt the user for performing library services information such borrow and return operations
        """
        while True:
            #obtain the name of the book and/or the ISBN of the book
            bookName = self.promptForBookName(False)
            bookISBN = self.promptForBookISBN(False)
        
            #if both are empty the user has cancelled the operation
            if len(bookName) == 0 and len(bookISBN) == 0:
                return None

            #try to obtain the book required by the user from the library using the book name
            if len(bookName) > 0:
                book = self._library.findBookByName(bookName)
                if book != None:
                    return book
                else:
                    print('The book was not found. Please select another book.')
            
            #try to obtain the book required by the user from the library using the book ISBN
            if len(bookISBN) > 0:
                book = self._library.findBookByISBN(bookISBN)
                if book != None:
                    return book
                else:
                    print('The book was not found. Please select another book.')                

    def manageBook(self, book):
        """Manage the book by allowing the user to execute operations on the given book
        Arguments:
            book - the book to be managed
        """
        while True:
            selBookMenuOpt = self.showBookMenu()

            if selBookMenuOpt == self.CHECK_STATUS_OPTION:
                self.onCheckBookStatus(book)
            elif selBookMenuOpt == self.BORROW_OPTION:
                self.onBorrowBook(book)
            elif selBookMenuOpt == self.RETURN_OPTION:
                self.onReturnBook(book)
            elif selBookMenuOpt == self.DISPLAY_BOOK_ASSETS:
                self.onDisplayBookAssets(book)
            elif selBookMenuOpt == self.EXIT_BOOK_MENU_OPTION:
                return
            else:
                print('Please enter a valid menu option')        

    def promptForBookName(self, isRequired = True):
        """
        Prompts the user to enter the name of the book and allows the user to cancel by pressing ENTER
        Returns:
            - the book name
        """
        bookName = input('Please enter the book name or press [ENTER] to cancel: ')
        
        if len(bookName) == 0 and isRequired:
            #the user has canceled the creation of the account
            raise OperationCancel('The user has selected to cancel the current operation')
        
        return bookName


    def promptForBookISBN(self, isRequired = True):
        """
        Prompts the user to enter the ISBN of the book and allows the user to cancel by pressing ENTER
        Returns:
            - the book ISBN         
        """
        bookISBN = input('Please enter the book ISBN or press [ENTER] to cancel: ')
        
        if len(bookISBN) == 0 and isRequired:
            #the user has canceled the creation of the account
            raise OperationCancel('The user has selected to cancel the current operation')
        
        return bookISBN

    def promptForBookAuthors(self):
        """Prompts the user to enter the authors of the book and allows the user to cancel by pressing ENTER"""
        print("Exercise: implement the intractivity necessary to prompt and obtain a list of authors")


    def promptForBookType(self):
        """
        Prompts the user to enter the type of book and allows the user to cancel by pressing ENTER
        Returns:
            - the book type as a constant        
        """
        print( "Exercise: implement the intractivity necessary to prompt and obtain the type of book (paper or digital)")

    def promptForBookCopies(self):
        """
        Prompts the user to enter the the number of copies of the book or to cancel by pressing ENTER
        Returns:
            - the number of copies to be entered in the library collection for the book being registered      
        """
        print( "Exercise: implement the intractivity necessary to prompt and obtain the number of copies for the book being registered")

    def onCheckBookStatus(self, book: Book):
        """
        Prints the status of the given book
        Arguments:
            book - the book for which the status is printed  
        """
        (isAvailable, nextAvailDate) = book.checkAvailability()
        if isAvailable:
            print(f"{book.getName()} is available.")
        else:
            print(f"{book.getName()} is not currently available. The book will be available on {nextAvailDate}. Would you like to reserve it?")
            userConf = input()
            if userConf.lower() == "yes":
                book.reserveBook()

    def onBorrowBook(self, book:Book):
        """
        Confirms the operation and performs the loan operation. Handles any errors related to incorrect 
        information
        Arguments:
            book - the book the library user would like to borrow
        """
        try:
            libAsset = book.borrowBook()
            print(f"The loan for'{book.getName()}' is confirmed.\nThe book is due on {libAsset.getDueDate()}. Please use ID {libAsset.getLibID()} when returning the book.")
        except InvalidTransaction as err:
            #the book could not be borrowed. The reason is in the exception object
            print(err, "\n")

    def onReturnBook(self, book):
        """
        Obtains necessary information, confirms the operation and performs the return operation. 
        Handles any errors related to incorrect information
        Arguments:
            book - the book the library user would like to return
        """
        while True:
            try:
                inputAmount = input('Please enter the library ID of the book you are returning or type [ENTER] to exit: ')
                
                #test for empty input in case the user pressed [ENTER] because they wanted to give up on withdrawing money
                if len(inputAmount) > 0:
                    libId = int(inputAmount)
                
                    #return the book asset using the ID provided by the user and check for late fees
                    (loanDuration, daysLate, lateFees) = book.returnBook(libId)
                    print(f"The book '{book.getName()}' was loaned for {loanDuration.days} days and was returned successfully.")

                    if daysLate > 0:
                        print(f"The book was late by {daysLate}. Please pay ${lateFees} at the cashier.")
                
                #the return was completed or user entered nothing so break from the infinite loop
                return

            except ValueError:
                #the user must have entered and invalid (e.g. "abc") amount
                print('Invalid entry. Please enter the library ID for the book you are returning.', "\n")

            except InvalidTransaction as err:
                #the book could not be returned. The reason is in the exception object
                print(err, "\n")      

    def onDisplayBookAssets(self, book: Book):
        """
        Displays all the library assets that correspond to the given book and their information such
        as whether they are available, loan and return dates, etc.
        Arguments:
            book - the book the librarian would like to see the details of
        """
        print(f"\n============== Library Asset Inventory ==================\n")
        print(f"Book Name: {book.getName()}")
        print(f"Author(s): {book.getAuthors()}")
        print(f"ISBN: {book.getISBN()}\n")
        
        print("Library Assets:")
        for libAsset in book.getAssets():
            if libAsset.getStatus() == LibraryAsset.AVAILABLE:
                print(f"\033[92m{libAsset.getLibID()}: available\033[0m")
            else:
                if libAsset.getLatePeriod().days > 0:
                    print(f"\033[91m{libAsset.getLibID()}: LATE, borrowed on {libAsset.getBorrowedOn()}",
                      f"due on {libAsset.getDueDate()} on loan for {libAsset.getLoanDuration().days} day(s), ",
                      f"late for {libAsset.getLatePeriod().days} day(s)\033[0m")                        
                else:
                    print(f"\033[93m{libAsset.getLibID()}: {libAsset.getStatus()}, borrowed on {libAsset.getBorrowedOn()}",
                        f"due on {libAsset.getDueDate()} on loan for {libAsset.getLoanDuration().days} days\033[0m")

