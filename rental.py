from movie import Movie


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """
    
    def __init__(self, movie, days_rented): 
    	"""Initialize a new movie rental object for
    	   a movie with known rental period (daysRented).
    	"""
    	self.movie = movie
    	self.days_rented = days_rented

    def get_movie(self):
    	return self.movie

    def get_days_rented(self):
    	return self.days_rented

    def get_price(self):
      return self.movie.get_price(self.days_rented)
    
    def get_rental_points(self):
      return self.movie.get_rental_points(self.days_rented)
    
    def rental_points(self):
        if self.get_movie().movie_type.category == "new_release":
                # New release earns 1 point per day rented
            return self.get_days_rented()
        else:
                # Other rentals get only 1 point
            return 1