using System.Collections.Generic;
using System.Linq;

namespace Proxy
{
    // Proxy Service
    public class LocalMovieSearcher : IMovieSearcher
    {
        List<Movie> localMovieDB;
        IMovieSearcher globalMovieSearcher;
        public LocalMovieSearcher(IMovieSearcher movieSearcher)
        {
            globalMovieSearcher = movieSearcher;
            localMovieDB = new List<Movie>()
            {
                new Movie() {Title="A1", Country = "Azerbaijan", Director = "Haci", Genre = "Action", Actors = "Maga"},
                new Movie() {Title="A2", Country = "Azerbaijan", Director = "Samur", Genre = "Dram", Actors = "Bred Pit"},
                new Movie() {Title="A3", Country = "Azerbaijan", Director = "Elesger", Genre = "Detective", Actors = "Benedict"}

            };
        }
        public Movie SearchByTitle(string title)
        {
            if (localMovieDB.Any(x => x.Title == title))
            {
                return localMovieDB.FirstOrDefault(x => x.Title == title);
            }
            else
            {
                return globalMovieSearcher.SearchByTitle(title);
            }
        }
    }
    
}
