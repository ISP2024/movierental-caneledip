from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract class for rental pricing."""
    # _instance = None

    # @classmethod
    # def __new__(cls):
    #     if not cls._instance:
    #         cls._instance = super(PriceStrategy, cls).__new__(cls)
    #     return cls._instance

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price for this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The points earned from this movie rental."""
        pass


class RegularPrice(PriceStrategy):
    """Rule for regular price strategy."""
    def get_price(self, days: int):
        """Regular price is 2 for 2 days, 1.5 for each days after."""
        if days > 2:
            return 2 + (days-2)*1.5
        return 2

    def get_rental_points(self, days: int):
        """Regular movie give 1 point per rental."""
        return 1


class ChildrenPrice(PriceStrategy):
    """Rule for children price strategy."""
    def get_price(self, days: int):
        """Children price is 1.5 for 3 days, 1.5 for each days after."""
        if days > 3:
            return 1.5 + (days-3)*1.5
        return 1.5

    def get_rental_points(self, days: int):
        """Children movie give 1 point per rental."""
        return 1


class NewReleasePrice(PriceStrategy):
    """Rule for new release price strategy."""
    def get_price(self, days: int):
        """New release price is 3 for each  days."""
        return days*3

    def get_rental_points(self, days: int):
        """New release movie give 1 point per days of rental."""
        return days
