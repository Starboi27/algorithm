DataA = [4, 29, 18, 13, 19, 25, 9, 6, 10, 24]
DataB = [18, 6, 23, 10, 27, 16, 11, 29, 13, 28, 9, 3, 15, 22, 19]

solve = []


def sort():

    for i in DataA:
        if i in DataB and i not in solve:
            solve.append(i)

    solve.sort()

    print(DataA)
    print(DataB)
    print(solve)


sort()

# 문제 걍 좆같이 냈네 진짜로 ㅅㅂ
