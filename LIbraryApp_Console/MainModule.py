"""
The starting module for Library App program that allows librarians to manage the books in a library
and provide library clients with library services.

Author: Prof. Magdin Stoica
E-Mail: magdin.stoica@sheridancollege.ca
Version 1.0 (Python)
"""

from LibraryApplicationModule import LibraryApplication

#create the application object
app = LibraryApplication()

#ask the app to run
app.run()