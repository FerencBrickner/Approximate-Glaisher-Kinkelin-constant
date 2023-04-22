from functools import reduce
import logging
from typing import Final, Generator
from types import MappingProxyType


def approx_glaisher_kinkelin_const(*, PRECISION: Final[int] = 22) -> float:
    n: int = PRECISION
    MAP_OF_TETRATED_NUMS: Final[map] = map(lambda i: i**i, range(n))
    H: Final[int] = reduce(lambda x, y: x * y, MAP_OF_TETRATED_NUMS)
    del MAP_OF_TETRATED_NUMS
    numerator: float = float(H)
    del H

    def approx_e_helper_function() -> float:
        NUMBER_OF_STEPS: Final[int] = 20
        fact: int = 1
        gen_fac: Generator[int, None, None] = (
            fact := fact * i for i in range(1, NUMBER_OF_STEPS + 1)
        )
        result: int = 1

        _ = [result := result + 1 / next(gen_fac) for _ in NUMBER_OF_STEPS * "."]
        return result

    EULER_NUMBER: Final[str] = approx_e_helper_function()
    n -= 1
    COEFFS = MappingProxyType({i: (0.5, 1 / 12)[not i] for i in range(3)})
    exponent: float = sum([n**i * c for i, c in COEFFS.items()])
    denominator: float = n**exponent
    denominator *= EULER_NUMBER ** (-n * n / 4)
    del EULER_NUMBER
    del n
    solution: float = numerator / denominator
    return solution


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info(approx_glaisher_kinkelin_const())
