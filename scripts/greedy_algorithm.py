"""貪欲法

1つのルールを繰り返し行う。
"""


def greedy_algorithm():
    s = 610
    medal_list = [500, 100, 50, 10, 5, 1]
    medal_cnt = [2, 0, 3, 1, 2, 3]

    cnt = 0
    for i in range(len(medal_list)):
        x = int(s / medal_list[i])
        cnt += x if x <= medal_cnt[i] else medal_cnt[i]
        s -= medal_list[i] * (x if x < medal_cnt[i] else medal_cnt[i])

        if s == 0:
            break

    print(cnt)


if __name__ == '__main__':
    greedy_algorithm()
