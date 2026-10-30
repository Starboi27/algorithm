import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\9_week_3\sample_input.txt", "r")

t = int(input())

for tc in range(t):
    x, y, r = map(int, input().split())
    print(x, y, r)
