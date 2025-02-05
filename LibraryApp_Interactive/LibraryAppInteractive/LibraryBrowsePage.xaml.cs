namespace LibraryAppInteractive;

public partial class LibraryBrowsePage : ContentPage
{
    /// <summary>
    /// The library instance gets initialized automaticaly to a single instance created by
    /// the MauiProgram class through "dependency injection"
    /// </summary>
    private Library _library;
    
    public LibraryBrowsePage(Library library)
    {
        //initialize the library to program's library single instance
        _library = library;
        
        InitializeComponent();
    }
}