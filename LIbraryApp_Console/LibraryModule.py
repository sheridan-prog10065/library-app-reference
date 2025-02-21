"""
Module that defines the Library class

Author: Prof. Magdin Stoica
E-Mail: magdin.stoica@sheridancollege.ca
Version 1.0 (Python)
"""
from BookModule import Book
from PaperBookModule import PaperBook
from DigitalBookModule import DigitalBook
from LibraryAssetModule import LibraryAsset

class Library:
    """
    Represents a collection of books in a library and provides business logic for library services

    Attributes:
        _bookList : list -- the list of books managed by the library

    Version 1.0 (Python)   
   """
    #these are class variables which are not specific to an instance, they are not field variables
    #they are shared by all instances and are accessible using the name of the class with the DOT notation
    
    """constants representing the type of book in the library collection"""
    BOOK_TYPE_PAPER = 1
    BOOK_TYPE_DIGITAL = 2
    BOOK_TYPE_AUDIO = 3

    """constant for the initial starting point for library asset IDs"""
    DEFAULT_LIBID_START = 100

    def __init__(self):
        """Initialize the field variables of the library collection object"""
        
        #create the list of books in the library collection
        self._bookList = []

        #define the starting point for the IDs given to library assets
        self._libIDGeneratorSeed = Library.DEFAULT_LIBID_START

        #create default books that are part of the library inventory
        self.createDefaultBooks()

    def createDefaultBooks(self):
        """
        Create 2 books with five library assets each so the application has something to work with
        even if no books are registered. New books can be registered by the user through the registration
        menu
        """
        #create a paper book
        demoPaperBook = PaperBook("Lord of the Rings", "978-0261102385")
        demoPaperBook.getAuthors().append("J.R.R. Tolkien")

        #add five library assets for this book
        for iAsset in range(5):
            #create the asset corresponding to this book
            demoBookAsset = LibraryAsset(self.determineLibraryID(), demoPaperBook)
            demoBookAsset.setStatus(LibraryAsset.AVAILABLE)

            #add the asset to the book
            demoPaperBook.getAssets().append(demoBookAsset)

        #add the book to the library
        self._bookList.append(demoPaperBook)

        #create a digital book
        demoDigitalBook = DigitalBook("Harry Potter", "978-1408898659")
        demoDigitalBook.getAuthors().append("J.K. Rowling")

        #add five library assets for this book
        for iAsset in range(5):
            #create the asset corresponding to this book
            demoBookAsset = LibraryAsset(self.determineLibraryID(), demoDigitalBook)
            demoBookAsset.setStatus(LibraryAsset.AVAILABLE)

            #add the asset to the book
            demoDigitalBook.getAssets().append(demoBookAsset)

        #add the book to the library
        self._bookList.append(demoDigitalBook)

    def findBookByName(self, bookName):
        """
        Returns the book with the given name or null if no book with that name can be found
        Parameters:
            name - the name of the book to return
        Return:
            the book object with the given name
        """ 
        #go through all the books in the list until one is found with the given book name
        for book in self._bookList:
            if book.getName() == bookName:
                return book
        
        #if the program got here it means there was no book with the given book name
        return None


    def findBookByISBN(self, isbn):
        """
        Returns the book with the given ISBN or null if no book with that ISBN can be found
        Parameters:
            isbn - the ISBN of the book to return
        Return:
            the book object with the given ISBN
        """ 
        #go through all the books in the list until one is found with the given book ISBN
        for book in self._bookList:
            if book.getISBN() == isbn:
                return book
        
        #if the program got here it means there was no book with the given book ISBN
        return None   

    def determineLibraryID(self):
        """Determine the a new library ID prompting the user until they enter the correct information
        
           The method will raise an AssertError if the user chooses to terminate.
        """   
        libId = self._libIDGeneratorSeed
        self._libIDGeneratorSeed += 1   
        return libId

    def registerBook(self, bookName, bookISBN, authors, bookType, nCopies):
        """
        Creates a new book with the given properties and book assets to match the number of copies provided
        Parameters:
            bookName - the name of the book
            bookISBN - the ISBN of the book
            authorrs - the list of authors for the book
            bookType - the type of book that is being registered
            nCopies  - the number of copies that are in the library collection for the registered book
        Returns:
            The book that was registered
        """
        assert(False, "Exercise: implement the business logic for creating and adding a new book")


