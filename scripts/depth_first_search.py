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
        return sum == k

    if dfs(i + 1, sum):
        return True

    if dfs(i + 1, sum + i_list[i]):
        return True

    return False


def main():
    print(dfs(0, 0))


if __name__ == '__main__':
    main()
