import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n, m, l = map(int, input().split())
    arr = [[x] for x in map(int, input().split())]
    for tm in range(m):
        i, j = map(int, input().split())
        arr[i].append(j)


print(arr)
