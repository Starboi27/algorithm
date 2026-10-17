# 재귀로 선택정렬 구현

Data = [3, 2, 5, 4, 1, 0]

howmany = len(Data)


def solve(now):

    if now == howmany - 1:
        return

    where = Data.index(min(Data[now:howmany]))
    Data[now], Data[where] = Data[where], Data[now]

    solve(now + 1)


solve(0)
print(Data)
