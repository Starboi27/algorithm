import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    datas = list(map(int, input().split()))
    count = 2
    best = 2
    for i in range(n - 2):

        if datas[i] == datas[i + 2]:
            count += 1
        else:
            count = 2

        best = max(count, best)

    print(best)

0, 2
1, 3
