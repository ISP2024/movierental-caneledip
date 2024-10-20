from movie import Movie
from enum import Enum
from price import *
from datetime import datetime


class Rental:
		"""
		A rental of a movie by customer.
		From Fowler's refactoring example.

		A realistic Rental would have fields for the dates
		that the movie was rented and returned, from which the
		rental period is calculated.
		For simplicity of this application only days_rented is recorded.
		"""

		NEW_RELEASE = NewReleasePrice()
		REGULAR = RegularPrice()
		CHILDREN = ChildrenPrice()

		@classmethod
		def price_code_for_movie(cls, movie: Movie):
			"""Determine a price code for movie, according to the year it released."""
			if 0 <= abs(datetime.year - movie.year) <= 1:
				 return NewReleasePrice()
			if movie.is_genre("Children") or movie.is_genre("Childrens"):
				 return ChildrenPrice()
			return RegularPrice()



		def __init__(self, movie, days_rented, price_code: PriceStrategy):
			"""Initialize a new movie rental object for
				 a movie with known rental period (daysRented).
			"""
			self.movie = movie
			self.days_rented = days_rented
			self.price_code = price_code

		def get_movie(self):
			return self.movie

		def get_days_rented(self):
			return self.days_rented
		
		def get_price_code(self):
			# get the price code
			return self.price_code_for_movie()

		def get_price(self):
			return self.get_price_code().get_price(self.days_rented)

		def get_rental_points(self):
			return self.get_price_code().get_rental_points(self.days_rented)

		# def rental_points(self):
		#     if self.get_movie().movie_type.category == "new_release":
		#             # New release earns 1 point per day rented
		#         return self.get_days_rented()
		#     else:
		#             # Other rentals get only 1 point
		#         return 1