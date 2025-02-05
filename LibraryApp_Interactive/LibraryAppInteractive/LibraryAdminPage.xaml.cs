using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LibraryAppInteractive;

public partial class LibraryAdminPage : ContentPage
{
    /// <summary>
    /// The library instance gets initialized automaticaly to a single instance created by
    /// the MauiProgram class through "dependency injection"
    /// </summary>    
    private Library _library;
    
    public LibraryAdminPage(Library library)
    {
        //initialize the library to program's library single instance
        _library = library;
        
        InitializeComponent();
    }
}