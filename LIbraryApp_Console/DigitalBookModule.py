"""
Module that defines the DigitalBook class

Author: Prof. Magdin Stoica
E-Mail: magdin.stoica@sheridancollege.ca
Version 1.0 (Python)
"""
from BookModule import Book
import random
from datetime import date, timedelta

class DigitalBook(Book):
    """
    Defines a digital book and its associated attributes and operations. The DigitalBook inherits all
    attributes and operations from the Book class and redefines some of the operations according
    to the business logic associated with the a digital book.

    Attributes:
        _maxBorrowDays      : int  -- the maximum loan duration for this book calculated based
                                   on particular license agreements (randomly generated)
        _latePenaltyPerDay  : float -- the late penalty per day for this book 

    Version 1.0 (Python)
    """

    def __init__(self, bookName, bookISBN):
        Book.__init__(self, bookName, bookISBN)

        #define the field variables associated witha digital book
        self._maxBorrowDays = 0
        self._latePenaltyPerDay = 0.0

        #calculate the values for maximum loand duration and maximum renews according to the
        #license agreement for this digital book
        self.determineLoanLicense()

    def determineLoanLicense(self):
        """
        Detrmines the values for maximum loan duration and maximum renews according to the
        license agreement for this digital book using randomly generated values according 
        the following business logic:
        The maximum loan duration in weeks is generated randomly to be number between 2 and 8 
        The late penalty is betwen 0.1 and 0.5         
        """
        self._maxBorrowDays = random.randint(2*7, 8*7)
        self._latePenaltyPerDay = 0.1 + random.random()* 0.4

    def borrowBook(self):
        """
        Overrides the base implementation to use the deadline and renewal conditions for paper books
        Returns:
            library asset that is loaned to the library users. The ID of the asset needs to be used to return the asset
        """
        #call the base implementation to borrow the book
        libAsset = Book.borrowBook(self)

        #adjust the due date according to the policy for paper books
        libAsset.setDueDate(date.today() + timedelta(days = self._maxBorrowDays))

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

        return (loanDuration, daysLate, daysLate * self._latePenaltyPerDay)