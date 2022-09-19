from __future__ import annotations
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [index for index, _ in sorted(
            ((index, sum(row)) for index, row in enumerate(mat)),
            key=lambda r: r[1]
        )[:k]]



if __name__ == '__main__':
    def main():
        example_1 = [[1, 1, 0, 0, 0],
                     [1, 1, 1, 1, 0],
                     [1, 0, 0, 0, 0],
                     [1, 1, 0, 0, 0],
                     [1, 1, 1, 1, 1]]
        print(Solution().kWeakestRows(example_1, k=3))

    main()
