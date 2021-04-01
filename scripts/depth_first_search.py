"""深さ優先探索(DFS)

ある状態から動作を続けて、遷移できなくなったら、1つ前に戻る、を繰り返す方法
"""
# n = 4
# i_list = [1, 2, 4, 7]
# k = 13

n = 4
i_list = [1, 2, 4, 7]
k = 15


def dfs(i: int, sum) -> bool:
    if i == n:
        # インデックスの最大値の場合、合計値と与えられたkが一致していたらTrueを返す
        return sum == k

    if dfs(i + 1, sum):
        # 現在のインデックスを足さないパターン
        return True

    if dfs(i + 1, sum + i_list[i]):
        # 現在のインデックスを足すパターン
        return True

    return False


def main():
    print(dfs(0, 0))


if __name__ == '__main__':
    main()
