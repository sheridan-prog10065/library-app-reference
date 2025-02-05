"""
Module that defines the Book class

Author: Prof. Magdin Stoica
E-Mail: magdin.stoica@sheridancollege.ca
Version 1.0 (Python)
"""
from LibraryAssetModule import LibraryAsset
from ExceptionsModule import InvalidTransaction
from datetime import date, timedelta

class Book:
    """
    Defines a book its associated attributes and operations.

    Attributes:
        _bookName        : str  -- the name of the book
        _bookISBN        : str  -- the ISBN of the book
        _bookAuthorsList : []   -- list of authors of the book. The list contains strings
        _libAssetList    : []   -- the list of actual library assets (physical books or 
                                           digital copies) for this book. 

    Version 1.0 (Python)
    """

    def __init__(self, bookName, bookISBN):
        """
        Initialize the book object with its attributes.

        The book constructor requires the caller to supply an book name and
        the book ISBN in order to create a book. 
     
        Arguments:
            bookName  : str   -- the book name, required parameter
            bookISBN  : str   -- the book ISBN, required parameter
        """
        self._bookName = bookName
        self._bookISBN = bookISBN
        self._bookAuthorsList =[]
        self._libAssetList = []
    
    def getName(self):
        """Returns the name of the book"""
        return self._bookName

    def getISBN(self):
        """Returns the ISBN of the book"""
        return self._bookISBN

    def getAuthors(self):
        """Returns the authors of the book"""
        return self._bookAuthorsList

    def getAssets(self):
        """Returns the library assets for this book (the actual copies that are part of library inventory)"""
        return self._libAssetList

    def checkAvailability(self):
        """
        Checks the availability of the book by checking if there are any library assets for this book that are available
        to load
        Returns:
            (true, None)            - an asset is availble and could be loaned
            (false, LibraryAsset)   - all assets for this book are either loaned or reserved. 
                                      The first asset to be available is at the provided to be reserved by the user
        """
        #find the next available asset. It could be available right away. If no asset is available right away
        #the earliest one is obtained
        nextAvailAsset = self.findNextAvailableAsset()

        if nextAvailAsset.getStatus() == LibraryAsset.AVAILABLE:
            return (True, None)
        else:      
            return (False, nextAvailAsset.getDueDate())

    def findLibraryAsset(self, libID):
        """Finds the library asset with the given ID. If no asset is found the method throws an exception"""
        for asset in self._libAssetList:
            #check if the asset ID matches the given iD
            if asset.getLibID() == libID:
                #the asset with the given lib ID was found
                return asset
        
        #if the code got to this point no asset was found which should not happen
        raise InvalidTransaction(f"An asset with ID = {libID} was not found for book {self.getName()}")
    
    def findNextAvailableAsset(self):
        """Finds the next available asset for this book"""
        nextAvailAsset = None
        for asset in self._libAssetList:
            #check if the asset is available
            if asset.getStatus() == LibraryAsset.AVAILABLE:
                #an asset is available right away
                return asset

            #check if the current asset has an earlier due date than the previously found one
            if nextAvailAsset == None or (nextAvailAsset.getDueDate() > asset.getDueDate() and 
                nextAvailAsset.getStatus() != LibraryAsset.RESERVED):
                nextAvailAsset = asset
        
        return nextAvailAsset
    
    def borrowBook(self):
        """
        Attempts to find an available asset and loans it to the user. If no book asset is available the method will
        throw an exception
        Returns:
            library asset that is loaned to the library users. The ID of the asset needs to be used to return the asset
        """
        #find the next available asset. 
        libraryAsset = self.findNextAvailableAsset()

        #check to make sure the book is available
        if libraryAsset.getStatus() != LibraryAsset.AVAILABLE:
            raise InvalidTransaction("The requested book is not available. You can check for availability first and reserve it.")
        
        #mark the asset as loaned
        libraryAsset.setBorrowedOn(date.today())
        libraryAsset.setStatus(LibraryAsset.LOANED)

        #set a default due date. This can be customized by derived classes
        libraryAsset.setDueDate(date.today() + timedelta(weeks = 2))

        return libraryAsset

    def returnBook(self, libID):
        """
        Returns a borrowed asset back to the library using the ID of the library asset. If the ID does not match an existing asset
        the method will throw an exception. Once returned, the library asset can be borrowed again. While
        the method can return late fees, the base method cannot calculate and it is left to derived classes
        Arguments:
            libID   - the ID of the library item being returned
        Returns:
            loan duration   - the duration of the loan as a timedelta object
            days late       - the number of days the book was late
            late fees       - the late fees applicable if any
        """
        #find the library asset being returned. If the ID is incorrect the transaction will be deemed invalid
        libraryAsset = self.findLibraryAsset(libID)
        libraryAsset.setReturnedOn(date.today())
        
        #obtain the loan data before reseting it to make the book available
        loanDuration = libraryAsset.getLoanDuration()
        latePeriod = libraryAsset.getLatePeriod()

        #make the asset available
        libraryAsset.setStatus(LibraryAsset.AVAILABLE)

        #the base method does not calculate any late penalties. Derived classes must perform the calculation
        #according to their specific business logic
        return (loanDuration, latePeriod.days, 0.0)

    def reserveBook(self):
        """Finds the earliest available asset that can be borrowed and reserves it"""
        #find the next available asset. It could be available right away. If no asset is available right away
        #the earliest one is obtained
        nextAvailAsset = self.findNextAvailableAsset()

        #mark teh asset as reserved
        nextAvailAsset.setStatus(LibraryAsset.RESERVED)

        #let the caller know what the reserved asset is
        return nextAvailAsset