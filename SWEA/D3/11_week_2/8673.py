import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")


t = int(input())

for tc in range(1, t + 1):
    k = int(input())
    arr = list(map(int, input().split()))
    result = 0

    while len(arr) > 1:
        winner = []

        for i in range((len(arr) // 2)):  # len = 4
            left = arr[i * 2]
            right = arr[(i * 2) + 1]

            if left > right:
                winner.append(left)
                result += left - right
            else:
                winner.append(right)
                result += right - left

        arr = winner

    print(f"#{tc} {result}")

# 재귀 사용법 복습
# 근데 stack을 써서 풀자
