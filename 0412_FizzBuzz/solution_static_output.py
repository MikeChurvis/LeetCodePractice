from __future__ import annotations
from typing import List


def generate_fizz_buzz_output(i: int) -> str:
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    if i % 3 == 0:
        return "Fizz"
    if i % 5 == 0:
        return "Buzz"

    return str(i)


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [generate_fizz_buzz_output(i+1) for i in range(n)]
