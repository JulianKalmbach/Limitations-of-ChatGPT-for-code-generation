from typing import Iterator, Any


def lines(path: str) -> Iterator[str]:
    with open(path) as f:
        for line in f:
            yield line


def parse_csv(lines: Iterator[str]) -> Iterator[list[str]]:
    for line in lines:
        yield line.replace('\n', '').split(',')


# Skip the next `n` elements produced by `xs`.
def skip(n: int, xs: Iterator[Any]) -> Iterator[Any]:
    for x in xs:
        if n > 0:
            n -= 1
        else:
            yield x


def update_balance(balance: float, csv_path: str) -> float:
    for row in skip(1, parse_csv(lines(csv_path))):
        balance += float(row[2])
    return balance


if __name__ == '__main__':
    print(update_balance(100, "umsatz.csv"))
    assert list(skip(3, range(5))) == [3, 4]
