from enum import Enum
from price import REGULAR, NEW_RELEASE, CHILDREN


class MovieType(Enum):
    # The types of movies.
    REGULAR = REGULAR
    NEW_RELEASE = NEW_RELEASE
    CHILDRENS = CHILDREN

    @property
    def price_code(self):
        return self.value

    @property
    def category(self):
        return self.name.lower()


class Movie:
    """
    A movie available for rent.
    """ 
    def __init__(self, title, movie_type: MovieType):
        # Initialize a new movie.
        if not isinstance(movie_type, MovieType):
            raise TypeError(f"Unrecognized movie type: {movie_type}")
        self.title = title
        self.movie_type = movie_type

    def get_price_code(self):
        # get the price code
        return self.movie_type.value
    
    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title

    def get_price(self, days: int):
        return self.get_price_code().get_price(days)

    def get_rental_points(self, days: int):
        return self.get_price_code().get_rental_points(days)