from __future__ import annotations
from typing import List


def generate_fizz_buzz_output(i: int) -> str:
    output = ""

    if i % 3 == 0:
        output += "Fizz"

    if i % 5 == 0:
        output += "Buzz"

    if len(output) == 0:
        output = str(i)

    return output


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [generate_fizz_buzz_output(i+1) for i in range(n)]
