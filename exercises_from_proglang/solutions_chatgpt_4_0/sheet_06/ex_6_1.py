from dataclasses import dataclass
from typing import Union, List
from datetime import datetime

# a) Datenklassen Food und NonFood
@dataclass
class Food:
    expiration_date: str  # Format "YYYY-MM-DD"

@dataclass
class NonFood:
    pass

@dataclass
class Stock:
    name: str
    units: int
    price_per_unit: int
    kind: Union[Food, NonFood]

# b) Funktion is_expired
def is_expired(stock: Stock, date: str) -> bool:
    if isinstance(stock.kind, Food):
        return stock.kind.expiration_date < date
    return False

# c) Funktion get_expired
def get_expired(stocks: List[Stock], date: str) -> List[Stock]:
    return [stock for stock in stocks if is_expired(stock, date)]

# d) Funktion buy
def buy(stock: Stock, quantity: int) -> int:
    if quantity > stock.units:
        bought_units = stock.units
        stock.units = 0
        return bought_units
    else:
        stock.units -= quantity
        return quantity