import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\10_week_5\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    N, M = map(int, input().split())
    Queue = list(map(int, input().split()))

    for i in range(M):
        here = Queue.pop(0)
        Queue.append(here)

    print(f"#{tc} {Queue[0]}")
