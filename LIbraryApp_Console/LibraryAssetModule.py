"""
Module that defines the LibraryAsset class

Author: Prof. Magdin Stoica
E-Mail: magdin.stoica@sheridancollege.ca
Version 1.0 (Python)
"""
from ExceptionsModule import InvalidTransaction
from datetime import date, timedelta

class LibraryAsset:
    """
    Defines a physical asset in the library such as a physical book copy or digital copy
    and its associated attributes and operations. Books are logical concepts in a library.
    Library users borrow and return library assets that corresponds to particular books.

    Attributes:
        _libID           : int  -- an internal library id that is used in asset inventory
        _book            : Book -- the book represented by this library asset 
        _status          : int  -- the status of the asset, whether it is available or not
        _borrowedOn      : date -- the date the book was borrowed on
        _returnedOn      : date -- the date the book was returned on
        _dueDate         : date -- the date the book is due

    Version 1.0 (Python)
    """

    #these are class variables which are not specific to an instance, they are not field variables
    #they are shared by all instances and are accessible using the name of the class with the DOT notation
    
    """constants representing the availability of a book"""
    NOT_AVAILABLE = 0
    AVAILABLE = 1
    LOANED = 2
    RESERVED = 3


    def __init__(self, libID, book):
        """
        Initialize the library asset with its attributes.

        The library asset constructor requires the caller to supply a library ID and the book
        this asset represents
     
        Arguments:
            libID   : int   -- the internal library ID of the asset
            book    : Book  -- the book this asset represents
        """
        self._libID = libID
        self._book = book
        self._status = LibraryAsset.NOT_AVAILABLE
        self._borrowedOn =  None
        self._returnedOn = None
        self._dueDate = None

    def getLibID(self):
        """Returns the ID of the library asset that can be used to uniquely identify the asset and return it
        upon borrowing"""
        return self._libID

    def getStatus(self):
        """Returns the status of the asset, whether it is available, on loan or reserved"""
        return self._status

    def setStatus(self, newStatus):
        """Modifies the status of the library asset to a new value"""
        self._status = newStatus

        if self._status == LibraryAsset.AVAILABLE:
            self._borrowedOn = None
            self._returnedOn = None
            self._dueDate = None


    def getBorrowedOn(self):
        """Returns the date the asset was borrowed on or null if the asset is not borrowed"""
        return self._borrowedOn

    def setBorrowedOn(self, borrowedDate):
        """Sets the date the asset was borrowed to the given date"""
        self._borrowedOn = borrowedDate

    def getReturnedOn(self):
        """Returns the date the asset was returned on"""
        return self._returnedOn

    def setReturnedOn(self, returnedDate):
        """Sets the returned date to the given date"""
        self._returnedOn = returnedDate

    def  getDueDate(self):
        """Returns the due-date the asset must be returned on"""
        return self._dueDate

    def setDueDate(self, newDueDate):
        self._dueDate = newDueDate

    def getLoanDuration(self):
        """Returns the duration of the loan if the book has been returned"""
        if self._borrowedOn == None:
            return timedelta()

        dateToCompare = date.today() if self._returnedOn == None else self._returnedOn

        return dateToCompare - self._borrowedOn

    def getLatePeriod(self):
        """Returns the late period if the book has been returned"""
        dateToCompare = date.today() if self._returnedOn == None else self._returnedOn

        if self._dueDate == None or dateToCompare < self._dueDate:
            return timedelta()
        else:
            return dateToCompare - self._dueDate 

    def isAvailable(self):
        """Checks whether the asset is available for borrowing by checking the status of the asset"""
        return self._status == LibraryAsset.AVAILABLE