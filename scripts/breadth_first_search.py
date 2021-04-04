"""幅優先探索(BFS)

深さ優先探索と同じく、辿り着ける全ての状態を生成する
メリット:
    同じ状態を通らない(DFSは通る)
デメリット:
    状態をメモリで保持しなければならない(DFSはBFSと比べて、保持する必要がある情報が少ないため、BFSより使用量が少ないと考えられる)

Queueを使う
Pythonドキュメント: https://docs.python.org/ja/3/library/queue.html
"""
from queue import Queue
from typing import List, Tuple

w = 10
h = 10

q_str = [
    '#S######.#',
    '......#..#',
    '.#.##.##.#',
    '.#........',
    '##.##.####',
    '....#....#',
    '.#######.#',
    '....#.....',
    '.####.###.',
    '....#...G#',
]

inf = w * h * 10
d_list = list(list(inf for i in range(w)) for j in range(h))


def bfs():
    x_move_list: List[int] = [0, 1, 0, -1]
    y_move_list: List[int] = [1, 0, -1, 0]
    s: Tuple[int, int]
    g: Tuple[int, int]

    for i, q in enumerate(q_str):
        for j, c in enumerate(q):
            if c == 'S':
                s = (i, j, 0)
                continue

            if c == 'G':
                g = (i, j)
                continue

    # Queue初期化、スタートの座標をTupleに入れる
    q: Queue = Queue()
    q.put(s)
    while not q.empty():
        # queueから取り出す
        x, y, d = q.get()

        for i in range(4):
            _x = x_move_list[i]
            _y = y_move_list[i]
            if x + _x >= 0 and x + _x < w and\
                    y + _y >= 0 and y + _y < h and\
                    q_str[y + _y][x + _x] != '#' and\
                    d_list[y + _y][x + _x] == inf:
                q.put((
                    x + x_move_list[i],
                    y + y_move_list[i],
                    d + 1,
                ))
                d_list[y + _y][x + _x] = d + 1

    print(d_list[g[0]][g[1]])


if __name__ == '__main__':
    bfs()
