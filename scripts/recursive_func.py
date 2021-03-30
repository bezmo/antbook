"""Fibonacci sequence
"""
from typing import List


def fibonacci(i: int) -> int:
    """フィボナッチ数列

    再起的に呼び出して計算する。
    i = 40 くらいの小さいと思われる数値でも計算量が大変多くなる。
    """
    if i == 1 or i == 0:
        return i
    return fibonacci(i - 1) + fibonacci(i - 2)


def fast_fibonacci(i: int) -> int:
    """高速化した(計算量を減らした)フィボナッチ数列

    一度計算した i 番目のフィボナッチ数列をメモ用の配列に入れる。
    配列のインデックスとフィボナッチ数列の i 番目を対応させること。
    """
    memo: List[int] = [0] * (i + 1)

    def _fibonacci(i):
        if i == 1 or i == 0:
            return i

        if memo[i] != 0:
            return memo[i]

        memo[i] = _fibonacci(i - 1) + _fibonacci(i - 2)
        return memo[i]

    return _fibonacci(i)


if __name__ == '__main__':
    print(fast_fibonacci(40))
