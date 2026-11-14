import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    data = list(input().strip())

    for idx in range(1, len(data)):
        first = data[:idx]
        second = data[idx : idx * 2]

        if first == second:
            total_len = idx
            break

    print(f"#{tc} {idx}")

# 인덱스 활용하기 복습 필요
