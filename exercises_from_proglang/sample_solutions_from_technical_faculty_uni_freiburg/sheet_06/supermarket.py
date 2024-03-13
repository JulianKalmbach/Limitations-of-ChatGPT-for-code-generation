from dataclasses import dataclass


# Data Types ##################################################################


@dataclass
class Food:
    expiration_date: str


@dataclass
class NonFood:
    pass


@dataclass
class Stock:
    name: str
    units: int
    price_per_unit: int
    kind: Food | NonFood

# Functions ###################################################################


def is_expired(stock: Stock, today: str) -> bool:
    match stock.kind:
        case Food():
            return today > stock.kind.expiration_date

    return False


def get_expired(stocks: list[Stock], today: str) -> list[Stock]:
    expired = []
    for stock in stocks:
        if is_expired(stock, today):
            expired += [stock]
    return expired


def buy(stock: Stock, units: int) -> int:
    bought_units = min(stock.units, units)
    stock.units -= bought_units
    return bought_units

# Tests #######################################################################


def test_supermarket():
    # test Stock
    stocks: list[Stock] = [
        Stock("Chocolate", 12, 199, Food("2020-12-07"), ),
        Stock("Tooth Brush", 30, 299, NonFood())
    ]
    print(f"Stocks: {stocks}")
    assert stocks[0].name == "Chocolate"
    assert stocks[0].units == 12
    assert stocks[0].price_per_unit == 199
    assert stocks[0].kind.expiration_date == "2020-12-07"

    assert stocks[1].name == "Tooth Brush"
    assert stocks[1].units == 30
    assert stocks[1].price_per_unit == 299

    # test get_expired
    assert get_expired(stocks, "2020-12-05") == []
    assert get_expired(stocks, "2020-12-09") == [stocks[0]]

    # test buy
    stock: Stock = Stock("Chocolate", 12, 199, Food("2020-12-07"))
    assert stock.units == 12
    assert buy(stock, 5) == 5
    assert stock.units == 7
    assert buy(stock, 25) == 7
    assert stock.units == 0


if __name__ == "__main__":
    test_supermarket()
