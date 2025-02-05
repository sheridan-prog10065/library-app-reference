using System.Collections.Immutable;

namespace LibraryAppInteractive;

public static class MauiProgram
{
    public static MauiApp CreateMauiApp()
    {
        var builder = MauiApp.CreateBuilder();
        builder
            .UseMauiApp<App>()
            .ConfigureFonts(fonts =>
            {
                fonts.AddFont("OpenSans-Regular.ttf", "OpenSansRegular");
                fonts.AddFont("OpenSans-Semibold.ttf", "OpenSansSemibold");
            });
        
        //Configure the services used in the application to share the library instance with the
        //two pages of the application. The single instance are passed to the constructor of the two pages
        //when they are created 
        builder.Services.AddSingleton<Library>();
        builder.Services.AddTransient<LibraryBrowsePage>();
        builder.Services.AddTransient<LibraryAdminPage>();

        return builder.Build();
    }
}