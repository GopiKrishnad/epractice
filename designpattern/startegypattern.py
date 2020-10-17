from abc import ABC, abstractmethod
import typing
from typing import Sequence, Optional, Callable


class Customer(typing.NamedTuple):
    name: str
    fidelity: int


class LineItem:
    def __init__(self, product: str, quantity: int, price: float):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    """Order take cart of items and promotion to be applied
    """
    def __init__(self, customer: Customer, cart: Sequence[LineItem], promotion: Optional['Promotion'] = None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0.0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):  # the Strategy: an abstract base class
    @abstractmethod
    def discount(self, order: Order) -> float:
        """Return discount on order"""
        pass


class FidelityPromo(Promotion):  # first Concrete Strategy
    """5% discount for customers with 1000 or more fidelity points"""
    def discount(self, order: Order) -> float:
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # second Concrete Strategy
    """10% discount for each LineItem with 20 or more units"""
    def discount(self, order: Order) -> float:
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.10
        return discount


class LargeOrderPromo(Promotion):  # third Concrete strategy
    """7% discount for orders with 10 or more distinct items"""
    def discount(self, order: Order) -> float:
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.7
        return 0


class BestOrderPromo:
    """promotion applied based on max discount"""
    def __init__(self):
        self.promotions = [FidelityPromo, BulkItemPromo, LargeOrderPromo]

    def discount(self, order: Order) -> float:
        return max(promotion.discount(self, order) for promotion in self.promotions)


if __name__ == "__main__":
    joe = Customer('John Doe',  0)
    ann = Customer('Ann Smith',  1100)
    cart = [LineItem('banana', 4, .5), LineItem('apple', 20, 1.5), LineItem('watermellon', 5, 5.0),
            LineItem('mango', 5, 6.0), LineItem('jack', 5, 5.5), LineItem('biki', 5, 1.5),
            LineItem('jiki', 5, 7.0), LineItem('tiki', 5, 8.0), LineItem('liki', 5, 6.0),
            LineItem('greenapple', 5, 9.0)]
    print(Order(joe, cart[:5], FidelityPromo()))
    print(Order(ann, cart, FidelityPromo()))
    print(Order(joe, cart[:5], BulkItemPromo()))
    print(Order(ann, cart, BulkItemPromo()))
    print(Order(joe, cart[:5], LargeOrderPromo()))
    print(Order(ann, cart, LargeOrderPromo()))
    print(Order(joe, cart[:5], BestOrderPromo()))
    print(Order(ann, cart, BestOrderPromo()))
