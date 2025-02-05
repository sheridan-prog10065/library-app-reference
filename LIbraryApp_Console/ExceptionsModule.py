"""
This module defines the user-defined exceptions used by the Library App program

Author: Prof. Magdin Stoica
E-Mail: magdin.stoica@sheridancollege.ca
Version 1.0 (Python)
"""

class OperationCancel(Exception): 
    """Exception used when the user cancels an operation by pressing ENTER"""
    pass

class InvalidTransaction(Exception):
     """Exception class used when an invalid trasaction is performed"""
     pass