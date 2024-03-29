#!/usr/bin/python3

"""N queens"""

import sys
from typing import List


def nqueens(n: int) -> List[List[int]]:
    """
    nqueens
    """
    col = set()
    posDiag = set()
    negDiag = set()
    board = []
    res = []

    def backtrack(r: int) -> List:
        """
        backtrack
        """
        if r == n:
            copy = board.copy()
            res.append(copy)
            return
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board.append([r, c])
            backtrack(r + 1)
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board.remove([r, c])

    backtrack(0)
    return res


if __name__ == "__main__":
    try:
        ar_sys = sys.argv[1]
        if not ar_sys.isnumeric():
            print("N must be a number")
        if int(sys.argv[1]) < 4:
            print("N must be at least 4")
        queens = nqueens(int(sys.argv[1]))
        for i in queens:
            print(i)
    except:
        print("Usage: nqueens N")
