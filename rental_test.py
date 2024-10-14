import unittest
from customer import Customer
from rental import Rental
from movie import Movie, MovieType


class RentalTest(unittest.TestCase):

	def setUp(self):
		self.new_movie = Movie("Dune: Part Two", MovieType.NEW_RELEASE)
		self.regular_movie = Movie("Air", MovieType.REGULAR)
		self.regular_movie = Movie("Air", MovieType.REGULAR)
		self.childrens_movie = Movie("Frozen", MovieType.CHILDRENS)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("Air", MovieType.REGULAR)
		self.assertEqual("Air", m.get_title())
		self.assertEqual(MovieType.REGULAR.value, m.get_price_code())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		rental = Rental(self.regular_movie, 1)
		self.assertEqual(rental.get_price(), 2.0)
		rental = Rental(self.regular_movie, 2)
		self.assertEqual(rental.get_price(), 2.0)
		rental = Rental(self.regular_movie, 3)
		self.assertEqual(rental.get_price(), 3.5)
		rental = Rental(self.childrens_movie, 1)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 3)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 5)
		self.assertEqual(rental.get_price(), 4.5)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.rental_points(), 5)
		rental = Rental(self.regular_movie, 1)
		self.assertEqual(rental.rental_points(), 1)
		rental = Rental(self.childrens_movie, 5)
		self.assertEqual(rental.rental_points(), 1)
		
