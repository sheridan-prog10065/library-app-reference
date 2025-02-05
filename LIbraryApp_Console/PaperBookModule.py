"""
Module that defines the PaperBook class

Author: Prof. Magdin Stoica
E-Mail: magdin.stoica@sheridancollege.ca
Version 1.0 (Python)
"""
from BookModule import Book
from datetime import date, timedelta

class PaperBook(Book):
    """
    Defines a paper book and its associated attributes and operations. The PaperBook inherits all
    attributes and operations from the Book class and redefines some of the operations according
    to the business logic associated with the a paper book.

    Attributes:
        - there are no specific attribute for this derived class

    Version 1.0 (Python)
    """

    #these are class variables which are not specific to an instance, they are not field variables
    #they are shared by all instances and are accessible using the name of the class with the DOT notation
    
    """constant representing maximum number of days a paper book can be borrowed"""
    MAX_BORROW_DAYS = 30

    """constant representing the late penalty per day that is applied to a late book"""
    LATE_PENALTY_PER_DAY = 0.25
    
    def __init__(self, bookName, bookISBN):
        Book.__init__(self, bookName, bookISBN)

    def borrowBook(self):
        """
        Overrides the base implementation to use the deadline and renewal conditions for paper books
        Returns:
            library asset that is loaned to the library users. The ID of the asset needs to be used to return the asset
        """
        #call the base implementation to borrow the book
        libAsset = Book.borrowBook(self)

        #adjust the due date according to the policy for paper books
        libAsset.setDueDate(date.today() + timedelta(days = PaperBook.MAX_BORROW_DAYS))

        return libAsset

    def returnBook(self, libID):
        """
        Returns a borrowed asset back to the library using the ID of the library asset. If the ID does not match an existing asset
        the method will throw an exception. Once returned, the library asset can be borrowed again. 

        Derived class overrides the base implementation to add late fees according to the policy for paper books
        Arguments:
            libID   - the ID of the library item being returned
        Returns:
            loan duration   - the duration of the loan as a timedelta object
            days late       - the number of days the book was late
            late fees       - the late fees applicable if any
        """
        #call the base implementation to borrow the book
        (loanDuration, daysLate, lateFees) = Book.returnBook(self, libID)

        return (loanDuration, daysLate, daysLate * PaperBook.LATE_PENALTY_PER_DAY)