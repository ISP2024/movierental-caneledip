"""Module used for Movie class."""
from dataclasses import dataclass
import logging
import csv


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """ 
    def __init__(self, title, year, genres):
        # Initialize a new movie.
        self.title = title
        self.year = year
        self.genres = genres

    def is_genre(self, other_genre: str):
        """Give a boolean if the string match any movie's genre."""
        for genre in self.genres:
            if genre.lower() == other_genre.lower():
                return True
        return False

    def get_title(self):
        """Give a title of a movie."""
        return self.title

    def __str__(self):
        return f"{self.title}({self.year})"


class MovieCatalog():
    """A catalog of movies from a csv file."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'movie_catalog'):  # Check if already initialized
            self.movie_catalog = []
            self.add_file_movies()

    def add_file_movies(self) -> None:
        """Load movies from CSV and store them as Movie objects."""
        try:
            with open('movies.csv', 'r') as movie_file:
                movie_csv = csv.reader(movie_file)
                header = next(movie_csv, None) # Skip header

                for row in movie_csv:
                    try:
                        title = row[1]
                        year = int(row[2])
                        genres = row[3].split("|")
                        self.movie_catalog.append(Movie(title=title, year=year, genres=genres))
                    except (ValueError, IndexError) as e:
                        log = logging.getLogger()
                        log.error(f"Error occured when processing row {row} - {e}.")
        except FileNotFoundError:
            log = logging.getLogger()
            log.error("Movies CSV file not found.")

    def get_movie(self, title: str, year: int = None) -> Movie:
        """Return the first movie matching the title (and optional year)."""
        for movie in self.movie_catalog:
            if movie.title == title and (year is None or movie.year == year):
                return movie
        return None
