"""Module used for Movie class."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """ 
    def __init__(self, title, year, genre):
        # Initialize a new movie.
        self.title = title
        self.year = year
        self.genre = genre

    def is_genre(self, other_genre: str):
        """Give a boolean if the string match any movie's genre."""
        return self.genre.lower_case() == other_genre.lower_case()

    def get_title(self):
        """Give a title of a movie."""
        return self.title

    def __str__(self):
        return f"{self.title}({self.year})"
