let movieNames = [
    "The Godfather",
    "The Shawshank Redemption",
    "The Dark Knight",
    "The Godfather: Part II",
    "12 Angry Men",
    "Schindler's List",
    "The Lord of the Rings: The Return of the King",
    "The Lord of the Rings: The Fellowship of the Ring",
    "Forrest Gump",
    "Star Wars: Episode V - The Empire Strikes Back",
    "Inception",
    "The Lord of the Rings: The Two Towers",
    "The Matrix",
    "Goodfellas",
    "One Flew Over the Cuckoo's Nest",
    "Seven Samurai",
    "Se7en",
    "City of God",
    "The Silence of the Lambs",
    "It's a Wonderful Life",
    "Life is Beautiful",
    "The Usual Suspects",
    "Saving Private Ryan",
    "Interstellar",
    "The Green Mile",
    "Léon: The Professional",
    "American History X",
    "The Prestige",
    "The Departed",
    "Gladiator",
    "Whiplash",
    "The Lion King",
    "Terminator 2: Judgment Day",
    "Back to the Future",
    "The Shining",
    "Alien",
    "Apocalypse Now",
    "The Intouchables",
    "The Terminator",
    "The Thing",
    "Eternal Sunshine of the Spotless Mind",
    "Die Hard",
    "Jurassic Park",
    "The Big Lebowski",
    "Blade Runner",
    "The Princess Bride",
    "The Exorcist",
    "The Silence of the Lambs",
    "The Godfather: Part III",
    "Full Metal Jacket",
    "Fight Club",
    "A Clockwork Orange",
    "No Country for Old Men",
    "The Magnificent Seven",
    "Raiders of the Lost Ark",
    "The Bridge on the River Kwai",
    "Lawrence of Arabia",
    "Singin' in the Rain",
    "Gandhi",
    "The French Connection",
    "The Sting",
    "Rocky",
    "Ben-Hur",
    "Chinatown",
    "Annie Hall",
    "The African Queen",
    "A Streetcar Named Desire",
    "On the Waterfront",
    "The Searchers",
    "The Maltese Falcon",
    "Casablanca",
    "Gone Girl",
    "The Social Network",
    "The Girl with the Dragon Tattoo",
    "Inglourious Basterds",
    "Django Unchained",
    "The Hateful Eight",
    "Kill Bill: Vol. 1",
    "Kill Bill: Vol. 2",
    "Reservoir Dogs",
    "Once Upon a Time in Hollywood",
    "True Romance",
    "Heat",
    "The Insider",
    "The Grand Budapest Hotel",
    "The Wolf of Wall Street",
    "Her",
    "Drive",
    "Moonlight",
    "La La Land",
    "Manchester by the Sea",
    "Birdman",
    "The Revenant",
    "The Big Short",
    "The Irishman",
    "Marriage Story",
    "The Handmaiden",
    "Parasite",
    "Snowpiercer",
    "Okja",
    "The Host",
    "Mother",
    "The Departures",
    "The Wind Rises",
    "Spirited Away",
    "Howl's Moving Castle",
    "My Neighbor Totoro",
    "The Lighthouse",
    "The Neon Demon",
    "The Killing of a Sacred Deer",
    "The Lobster",
    "Uncut Gems",
    "The Meyerowitz Stories",
    "Frances Ha",
    "Lady Bird",
    "Moonrise Kingdom",
    "The Royal Tenenbaums",
    "Isle of Dogs",
    "The Grandmaster",
    "The Assassin",
    "Crouching Tiger, Hidden Dragon",
    "Hard Boiled",
    "Hero",
    "Raise the Red Lantern",
    "Farewell My Concubine",
    "House of Flying Daggers",
    "The Hand of Fate",
    "Blade of the Immortal",
    "Seven Swords",
    "Red Cliff",
    "Shutter Island",
    "Prisoners",
    "The Girl on the Train",
    "Gone Baby Gone",
    "Mystic River",
    "Memento",
    "Following",
    "Insomnia",
    "The Batman",
    "Wonder Woman",
    "The Avengers",
    "Iron Man",
    "Black Panther",
    "Spider-Man: Into the Spider-Verse",
    "Guardians of the Galaxy",
    "Thor: Ragnarok",
    "Doctor Strange",
    "Captain Marvel",
    "The Dark Knight Rises",
    "The Amazing Spider-Man",
    "The Hunger Games",
    "The Maze Runner",
    "The Divergent Series",
    "The Fault in Our Stars",
    "The Perks of Being a Wallflower",
    "Me and Earl and the Dying Girl",
    "The Spectacular Now",
    "The Descendants",
    "The Florida Project",
    "The Squid and the Whale",
    "Moon",
    "Source Code",
    "District 9",
    "Elysium",
    "Chappie",
    "Children of Men",
    "V for Vendetta",
    "Equilibrium",
    "The Road",
    "The Fifth Element",
    "Ex Machina",
    "Hereditary",
    "Midsommar",
    "The Witch",
    "Us",
    "Get Out",
    "Split",
    "The Babadook",
    "It Follows",
    "The Shape of Water",
    "Pan's Labyrinth",
    "Hellboy",
    "Pacific Rim"];

var MOVIES = [];
const genresSection = document.getElementById("genres");
genresSection.style.height = '90VH';
const moviesSection = document.getElementById("movies");
const searchText = document.getElementById("searchText");
const searchButton = document.getElementById('searchBtn');

searchButton.addEventListener('click', function (event) {
    event.preventDefault();
    searchMovie();
});

async function getMovieData(title, all = 't') {
    const urls = [
        `http://www.omdbapi.com/?apikey=d5254632&${all}=${title}&plot=full`,
        `http://www.omdbapi.com/?apikey=33e21c84&${all}=${title}&plot=full`,
        `http://www.omdbapi.com/?apikey=ddee1dae&${all}=${title}&plot=full`,
    ];

    let resp;
    for (const url of urls) {
        const response = await fetch(url);
        const data = await response.json();
        if (data.Response !== 'False') {
            return data;
        }
        else if (data.Error){
            resp = data.Error;
        }
    }

    if (resp)
        return resp;

    return 'No results found';
}

async function getMovies(movieNames) {
    const promises = movieNames.map(name => getMovieData(name));
    try {
        const movies = await Promise.all(promises);
        return movies.filter(m => m.Genre != undefined && m.Genre != 'N/A').filter(g => g.Poster != undefined && g.Poster != 'N/A');
    } catch (error) {
        console.error(error);
        return [];
    }
}

function getGenres() {
    let allGenres = [];
    MOVIES.forEach(m => {
        if (m.Genre) {
            let genres = m.Genre.split(',');
            genres.forEach(g => {
                allGenres.push(g.trim());
            });
        }
    });
    return [...new Set(allGenres)];
}

function showMoviesByGenre(genre) {
    moviesSection.innerHTML = `<h1 id="titleOfMovies">${genre}</h1>`;
    let movies = MOVIES.filter(m => m.Genre.includes(genre));
    movies.forEach(m => {
        if (m.Poster) {
            let content = `
                <section id='movie'>
                <img src='${m.Poster}' alt='${m.Title}' class="img-fluid">
                </section>`;
            moviesSection.innerHTML += content;
        };
    });
}

function addAllMovies() {
    moviesSection.innerHTML = '<h1 id="titleOfMovies">All Movies</h1>';
    MOVIES.forEach(m => {
        if (m.Poster) {
            let content = `
                <section id='movie'>
                <img src='${m.Poster}' alt='${m.Title}' class="img-fluid">
                </section>`;
            moviesSection.innerHTML += content;
        };
    });
}

async function searchMovie() {
    moviesSection.innerHTML = '<section class="spinner-border" style="margin:auto; color: #F46C38 !important;" role="status"><span class="visually-hidden">Loading...</span></section>';
    let movieTitle = searchText.value;
    let response = await getMovieData(movieTitle, 's');
    let movies;
    if (response) {
        if (response.Search)
            movies = response.Search.filter(g => g.Poster != undefined && g.Poster != 'N/A');
    }
    if (movies) {
        moviesSection.innerHTML = `<h1 id="titleOfMovies">${movieTitle}</h1>`;
    }
    else {
        moviesSection.innerHTML = `<h1 id="titleOfMovies">${response}</h1>`;
        return;
    }
    movies.forEach(m => {
        if (m.Poster) {
            let content = `
                <section id='movie'>
                <img src='${m.Poster}' alt='${m.Title}' class="img-fluid">
                </section>`;
            moviesSection.innerHTML += content;
        };
    });
}

(async function () {
    genresSection.innerHTML = '<section class="spinner-border" style="margin:auto; margin-top: 20px; margin-bottom:20px; color: #F46C38 !important;" role="status"><span class="visually-hidden">Loading...</span></section>';
    moviesSection.innerHTML = '<section class="spinner-border" style="margin:auto; color: #F46C38 !important;" role="status"><span class="visually-hidden">Loading...</span></section>';
    MOVIES = await getMovies(movieNames);
    console.log(MOVIES);

    // Add Genres
    const genres = getGenres();
    genresSection.style.height = 'AUTO';
    genresSection.innerHTML = '';
    genres.forEach(g => {
        let content = `
        <li class="nav-item">
            <a class="nav-link" aria-current="page" href="#" style='cursor:pointer; margin-left:10px !important;' onclick='showMoviesByGenre("${g}")'>
              ${g}
            </a>
        </li>`;
        genresSection.innerHTML += content;
    });

    // Add Movies
    addAllMovies();
})();